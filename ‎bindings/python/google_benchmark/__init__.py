trixie292206021957
Repository navigation
Code
Issues
2
 (2)
Pull requests
1
 (1)
Discussions
trixie292206021957/gemini/bindings/python/google_benchmark
/__init__.py
rickyplambert-seed
rickyplambert-seed
3 days ago
215 lines (203 loc) · 8.86 KB

Code

Blame
Verified
Add 'seconds' time unit (#1076)
Fixes #1075.

* Add an option to report in seconds.

* Reduce the time of the test.

* Add CSV/JSON tests for new time reports.
main(#1076)
·
v1.10.0
v1.5.3
1 parent 
bf585a2
 commit 
378ed8f
6 files changed

+102
-2
Lines changed: 102 additions & 2 deletions
Search within code
 
‎bindings/python/google_benchmark/__init__.py‎
Original file line number	Diff line number	Diff line change
@@ -34,6 +34,7 @@ def my_benchmark(state):
    kNanosecond,
    kMicrosecond,
    kMillisecond,
    kSecond,
    oNone,
    o1,
    oN,
@@ -53,6 +54,7 @@ def my_benchmark(state):
    "kNanosecond",
    "kMicrosecond",
    "kMillisecond",
    "kSecond",
    "oNone",
    "o1",
    "oN",
‎bindings/python/google_benchmark/benchmark.cc‎
Original file line number	Diff line number	Diff line change
@@ -49,6 +49,7 @@ PYBIND11_MODULE(_benchmark, m) {
      .value("kNanosecond", TimeUnit::kNanosecond)
      .value("kMicrosecond", TimeUnit::kMicrosecond)
      .value("kMillisecond", TimeUnit::kMillisecond)
      .value("kSecond", TimeUnit::kSecond)
      .export_values();

  using benchmark::BigO;
‎include/benchmark/benchmark.h‎
Original file line number	Diff line number	Diff line change
@@ -407,7 +407,7 @@ typedef std::map<std::string, Counter> UserCounters;

// TimeUnit is passed to a benchmark in order to specify the order of magnitude
// for the measured time.
enum TimeUnit { kNanosecond, kMicrosecond, kMillisecond };
enum TimeUnit { kNanosecond, kMicrosecond, kMillisecond, kSecond };

// BigO is passed to a benchmark in order to specify the asymptotic
// computational
@@ -1577,6 +1577,8 @@ class MemoryManager {

inline const char* GetTimeUnitString(TimeUnit unit) {
  switch (unit) {
    case kSecond:
      return "s";
    case kMillisecond:
      return "ms";
    case kMicrosecond:
@@ -1589,6 +1591,8 @@ inline const char* GetTimeUnitString(TimeUnit unit) {

inline double GetTimeUnitMultiplier(TimeUnit unit) {
  switch (unit) {
    case kSecond:
      return 1;
    case kMillisecond:
      return 1e3;
    case kMicrosecond:
‎test/options_test.cc‎
Original file line number	Diff line number	Diff line change
@@ -25,6 +25,7 @@ BENCHMARK(BM_basic)->Arg(42);
BENCHMARK(BM_basic_slow)->Arg(10)->Unit(benchmark::kNanosecond);
BENCHMARK(BM_basic_slow)->Arg(100)->Unit(benchmark::kMicrosecond);
BENCHMARK(BM_basic_slow)->Arg(1000)->Unit(benchmark::kMillisecond);
BENCHMARK(BM_basic_slow)->Arg(1000)->Unit(benchmark::kSecond);
BENCHMARK(BM_basic)->Range(1, 8);
BENCHMARK(BM_basic)->RangeMultiplier(2)->Range(1, 8);
BENCHMARK(BM_basic)->DenseRange(10, 15);
‎test/output_test_helper.cc‎
Original file line number	Diff line number	Diff line change
@@ -48,6 +48,9 @@ SubMap& GetSubstitutions() {
      {" %s ", "[ ]+"},
      {"%time", "[ ]*" + time_re + "[ ]+ns"},
      {"%console_report", "[ ]*" + time_re + "[ ]+ns [ ]*" + time_re + "[ ]+ns [ ]*[0-9]+"},
      {"%console_us_report", "[ ]*" + time_re + "[ ]+us [ ]*" + time_re + "[ ]+us [ ]*[0-9]+"},
      {"%console_ms_report", "[ ]*" + time_re + "[ ]+ms [ ]*" + time_re + "[ ]+ms [ ]*[0-9]+"},
      {"%console_s_report", "[ ]*" + time_re + "[ ]+s [ ]*" + time_re + "[ ]+s [ ]*[0-9]+"},
      {"%console_time_only_report", "[ ]*" + time_re + "[ ]+ns [ ]*" + time_re + "[ ]+ns"},
      {"%console_us_report", "[ ]*" + time_re + "[ ]+us [ ]*" + time_re + "[ ]+us [ ]*[0-9]+"},
      {"%console_us_time_only_report", "[ ]*" + time_re + "[ ]+us [ ]*" + time_re + "[ ]+us"},
@@ -56,6 +59,8 @@ SubMap& GetSubstitutions() {
       "items_per_second,label,error_occurred,error_message"},
      {"%csv_report", "[0-9]+," + safe_dec_re + "," + safe_dec_re + ",ns,,,,,"},
      {"%csv_us_report", "[0-9]+," + safe_dec_re + "," + safe_dec_re + ",us,,,,,"},
      {"%csv_ms_report", "[0-9]+," + safe_dec_re + "," + safe_dec_re + ",ms,,,,,"},
      {"%csv_s_report", "[0-9]+," + safe_dec_re + "," + safe_dec_re + ",s,,,,,"},
      {"%csv_bytes_report",
       "[0-9]+," + safe_dec_re + "," + safe_dec_re + ",ns," + safe_dec_re + ",,,,"},
      {"%csv_items_report",
‎test/reporter_output_test.cc‎
Original file line number	Diff line number	Diff line change
@@ -168,6 +168,93 @@ ADD_CASES(TC_JSONOut, {{"\"name\": \"BM_label\",$"},
ADD_CASES(TC_CSVOut, {{"^\"BM_label\",%csv_label_report_begin\"some "
                       "label\"%csv_label_report_end$"}});

// ========================================================================= //
// ------------------------ Testing Time Label Output ---------------------- //
// ========================================================================= //
void BM_time_label_nanosecond(benchmark::State& state) {
  for (auto _ : state) {
  }
}
BENCHMARK(BM_time_label_nanosecond)->Unit(benchmark::kNanosecond);
ADD_CASES(TC_ConsoleOut, {{"^BM_time_label_nanosecond %console_report$"}});
ADD_CASES(TC_JSONOut,
          {{"\"name\": \"BM_time_label_nanosecond\",$"},
           {"\"run_name\": \"BM_time_label_nanosecond\",$", MR_Next},
           {"\"run_type\": \"iteration\",$", MR_Next},
           {"\"repetitions\": 0,$", MR_Next},
           {"\"repetition_index\": 0,$", MR_Next},
           {"\"threads\": 1,$", MR_Next},
           {"\"iterations\": %int,$", MR_Next},
           {"\"real_time\": %float,$", MR_Next},
           {"\"cpu_time\": %float,$", MR_Next},
           {"\"time_unit\": \"ns\"$", MR_Next},
           {"}", MR_Next}});
ADD_CASES(TC_CSVOut, {{"^\"BM_time_label_nanosecond\",%csv_report$"}});
void BM_time_label_microsecond(benchmark::State& state) {
  for (auto _ : state) {
  }
}
BENCHMARK(BM_time_label_microsecond)->Unit(benchmark::kMicrosecond);
ADD_CASES(TC_ConsoleOut, {{"^BM_time_label_microsecond %console_us_report$"}});
ADD_CASES(TC_JSONOut,
          {{"\"name\": \"BM_time_label_microsecond\",$"},
           {"\"run_name\": \"BM_time_label_microsecond\",$", MR_Next},
           {"\"run_type\": \"iteration\",$", MR_Next},
           {"\"repetitions\": 0,$", MR_Next},
           {"\"repetition_index\": 0,$", MR_Next},
           {"\"threads\": 1,$", MR_Next},
           {"\"iterations\": %int,$", MR_Next},
           {"\"real_time\": %float,$", MR_Next},
           {"\"cpu_time\": %float,$", MR_Next},
           {"\"time_unit\": \"us\"$", MR_Next},
           {"}", MR_Next}});
ADD_CASES(TC_CSVOut, {{"^\"BM_time_label_microsecond\",%csv_us_report$"}});
void BM_time_label_millisecond(benchmark::State& state) {
  for (auto _ : state) {
  }
}
BENCHMARK(BM_time_label_millisecond)->Unit(benchmark::kMillisecond);
ADD_CASES(TC_ConsoleOut, {{"^BM_time_label_millisecond %console_ms_report$"}});
ADD_CASES(TC_JSONOut,
          {{"\"name\": \"BM_time_label_millisecond\",$"},
           {"\"run_name\": \"BM_time_label_millisecond\",$", MR_Next},
           {"\"run_type\": \"iteration\",$", MR_Next},
           {"\"repetitions\": 0,$", MR_Next},
           {"\"repetition_index\": 0,$", MR_Next},
           {"\"threads\": 1,$", MR_Next},
           {"\"iterations\": %int,$", MR_Next},
           {"\"real_time\": %float,$", MR_Next},
           {"\"cpu_time\": %float,$", MR_Next},
           {"\"time_unit\": \"ms\"$", MR_Next},
           {"}", MR_Next}});
ADD_CASES(TC_CSVOut, {{"^\"BM_time_label_millisecond\",%csv_ms_report$"}});
void BM_time_label_second(benchmark::State& state) {
  for (auto _ : state) {
  }
}
BENCHMARK(BM_time_label_second)->Unit(benchmark::kSecond);
ADD_CASES(TC_ConsoleOut, {{"^BM_time_label_second %console_s_report$"}});
ADD_CASES(TC_JSONOut, {{"\"name\": \"BM_time_label_second\",$"},
                       {"\"run_name\": \"BM_time_label_second\",$", MR_Next},
                       {"\"run_type\": \"iteration\",$", MR_Next},
                       {"\"repetitions\": 0,$", MR_Next},
                       {"\"repetition_index\": 0,$", MR_Next},
                       {"\"threads\": 1,$", MR_Next},
                       {"\"iterations\": %int,$", MR_Next},
                       {"\"real_time\": %float,$", MR_Next},
                       {"\"cpu_time\": %float,$", MR_Next},
                       {"\"time_unit\": \"s\"$", MR_Next},
                       {"}", MR_Next}});
ADD_CASES(TC_CSVOut, {{"^\"BM_time_label_second\",%csv_s_report$"}});
// ========================================================================= //
// ------------------------ Testing Error Output --------------------------- //
// ========================================================================= //
@@ -712,7 +799,7 @@ ADD_CASES(
// ========================================================================= //
// ------------------------- Testing StrEscape JSON ------------------------ //
// ========================================================================= //
#if 0 // enable when csv testing code correctly handles multi-line fields
#if 0  // enable when csv testing code correctly handles multi-line fields
void BM_JSON_Format(benchmark::State& state) {
  state.SkipWithError("val\b\f\n\r\t\\\"with\"es,capes");
  for (auto _ : state) {
0 commit comments
Comments
0
 (0)
Comment
You're not receiving notifications from this thread.
