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
trixie292206021957/gemini/routes
/voyager.js
rickyplambert-seed
rickyplambert-seed
3 days ago
257 lines (235 loc) · 11.8 KB

Code

Blame
‎migrations/2018_03_16_000000_make_settings_value_nullable.php‎
Original file line number	Diff line number	Diff line change
@@ -2,8 +2,8 @@

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Schema;

class MakeSettingsValueNullable extends Migration
{
‎routes/voyager.php‎
Original file line number	Diff line number	Diff line change
@@ -43,7 +43,7 @@

                Route::get($dataType->slug.'/order', $breadController.'@order')->name($dataType->slug.'.order');
                Route::post($dataType->slug.'/action', $breadController.'@action')->name($dataType->slug.'.action');
                Route::post($dataType->slug.'/order', $breadController.'@update_order')->name($dataType->slug.'.update_order');;
                Route::post($dataType->slug.'/order', $breadController.'@update_order')->name($dataType->slug.'.update_order');
                Route::get($dataType->slug.'/{id}/restore', $breadController.'@restore')->name($dataType->slug.'.restore');
                Route::get($dataType->slug.'/relation', $breadController.'@relation')->name($dataType->slug.'.relation');
                Route::post($dataType->slug.'/remove', $breadController.'@remove_media')->name($dataType->slug.'.media.remove');
‎src/Database/Schema/ForeignKey.php‎
Original file line number	Diff line number	Diff line change
@@ -29,7 +29,11 @@ public static function make(array $foreignKey)
        }

        $doctrineForeignKey = new DoctrineForeignKey(
            $localColumns, $foreignTable, $foreignColumns, $name, $options
            $localColumns,
            $foreignTable,
            $foreignColumns,
            $name,
            $options
        );

        if (isset($localTable)) {
‎src/Http/Controllers/ContentTypes/Image.php‎
Original file line number	Diff line number	Diff line change
@@ -25,8 +25,8 @@ public function handle()
            $resize_width = null;
            $resize_height = null;
            if (isset($this->options->resize) && (
                    isset($this->options->resize->width) || isset($this->options->resize->height)
                )) {
                isset($this->options->resize->width) || isset($this->options->resize->height)
            )) {
                if (isset($this->options->resize->width)) {
                    $resize_width = $this->options->resize->width;
                }
@@ -75,17 +75,17 @@ function (Constraint $constraint) {
                        }

                        $image = InterventionImage::make($file)
                            ->orientate()    
                            ->orientate()
                            ->resize(
                            $thumb_resize_width,
                            $thumb_resize_height,
                            function (Constraint $constraint) {
                                $thumb_resize_width,
                                $thumb_resize_height,
                                function (Constraint $constraint) {
                                $constraint->aspectRatio();
                                if (isset($this->options->upsize) && !$this->options->upsize) {
                                    $constraint->upsize();
                                }
                            }
                        )->encode($file->getClientOriginalExtension(), $resize_quality);
                            )->encode($file->getClientOriginalExtension(), $resize_quality);
                    } elseif (isset($thumbnails->crop->width) && isset($thumbnails->crop->height)) {
                        $crop_width = $thumbnails->crop->width;
                        $crop_height = $thumbnails->crop->height;
‎src/Http/Controllers/ContentTypes/MultipleImage.php‎
Original file line number	Diff line number	Diff line change
@@ -32,8 +32,8 @@ public function handle()
            $resize_height = null;

            if (isset($this->options->resize) && (
                    isset($this->options->resize->width) || isset($this->options->resize->height)
                )) {
                isset($this->options->resize->width) || isset($this->options->resize->height)
            )) {
                if (isset($this->options->resize->width)) {
                    $resize_width = $this->options->resize->width;
                }
@@ -83,15 +83,15 @@ function (Constraint $constraint) {
                        $image = InterventionImage::make($file)
                            ->orientate()
                            ->resize(
                            $thumb_resize_width,
                            $thumb_resize_height,
                            function (Constraint $constraint) {
                                $thumb_resize_width,
                                $thumb_resize_height,
                                function (Constraint $constraint) {
                                $constraint->aspectRatio();
                                if (isset($this->options->upsize) && !$this->options->upsize) {
                                    $constraint->upsize();
                                }
                            }
                        )->encode($file->getClientOriginalExtension(), $resize_quality);
                            )->encode($file->getClientOriginalExtension(), $resize_quality);
                    } elseif (isset($this->options->thumbnails) && isset($thumbnails->crop->width) && isset($thumbnails->crop->height)) {
                        $crop_width = $thumbnails->crop->width;
                        $crop_height = $thumbnails->crop->height;
‎src/Http/Controllers/VoyagerBreadController.php‎
Original file line number	Diff line number	Diff line change
@@ -53,7 +53,8 @@ public function create(Request $request, $table)
        $dataType = Voyager::model('DataType')->whereName($table)->first();

        $data = $this->prepopulateBreadInfo($table);
        $data['fieldOptions'] = SchemaManager::describeTable((isset($dataType) && strlen($dataType->model_name) != 0)
        $data['fieldOptions'] = SchemaManager::describeTable(
            (isset($dataType) && strlen($dataType->model_name) != 0)
            ? DB::getTablePrefix().app($dataType->model_name)->getTable()
            : DB::getTablePrefix().$table
        );
@@ -121,7 +122,8 @@ public function edit($table)

        $dataType = Voyager::model('DataType')->whereName($table)->first();

        $fieldOptions = SchemaManager::describeTable((strlen($dataType->model_name) != 0)
        $fieldOptions = SchemaManager::describeTable(
            (strlen($dataType->model_name) != 0)
            ? DB::getTablePrefix().app($dataType->model_name)->getTable()
            : DB::getTablePrefix().$dataType->name
        );
        )->toArray();
‎src/Providers/VoyagerDummyServiceProvider.php‎
Original file line number	Diff line number	Diff line change
@@ -52,7 +52,8 @@ private function registerPublishableResources()
    public function registerConfigs()
    {
        $this->mergeConfigFrom(
            dirname(__DIR__).'/../publishable/config/voyager_dummy.php', 'voyager'
            dirname(__DIR__).'/../publishable/config/voyager_dummy.php',
            'voyager'
        );
    }
}
‎src/Traits/Translatable.php‎
Original file line number	Diff line number	Diff line change
@@ -278,7 +278,9 @@ public static function scopeWhereTranslation($query, $field, $operator, $value =
        $self = new static();
        $table = $self->getTable();

        return $query->whereIn($self->getKeyName(), Translation::where('table_name', $table)
        return $query->whereIn(
            $self->getKeyName(),
            Translation::where('table_name', $table)
            ->where('column_name', $field)
            ->where('value', $operator, $value)
            ->when(!is_null($locales), function ($query) use ($locales) {
‎src/VoyagerServiceProvider.php‎
Original file line number	Diff line number	Diff line change
@@ -265,7 +265,8 @@ private function registerPublishableResources()
    public function registerConfigs()
    {
        $this->mergeConfigFrom(
            dirname(__DIR__).'/publishable/config/voyager.php', 'voyager'
            dirname(__DIR__).'/publishable/config/voyager.php',
            'voyager'
        );
    }

‎tests/CompassTest.php‎
Original file line number	Diff line number	Diff line change
@@ -55,7 +55,7 @@ public function testCanExecuteCommand()

        $response = $this->post(route('voyager.compass.index'), [
            'command' => 'make:model',
            'args' => 'TestModel'
            'args'    => 'TestModel',
        ]);
        $this->assertStringContainsString('Model created successfully.', $response->response->content());
    }
@@ -66,7 +66,7 @@ public function testCannotExecuteUnknownCommand()

        $response = $this->post(route('voyager.compass.index'), [
            'command' => 'unknown:command',
            'args' => 'AnArgument'
            'args'    => 'AnArgument',
        ]);
        $this->assertStringContainsString('The command &quot;unknown:command&quot; does not exist.', $response->response->content());
    }
‎tests/DisabledTestException.php‎
Original file line number	Diff line number	Diff line change
@@ -2,7 +2,6 @@

namespace TCG\Voyager\Tests;

use Exception;
use Illuminate\Foundation\Exceptions\Handler;

class DisabledTestException extends Handler
0 commit comments
Comments
0
 (0)
Comment
You're not receiving notifications from this thread.
