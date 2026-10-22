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
trixie292206021957/gemini
/rickylambert.txt
rickyplambert-seed
rickyplambert-seed
3 days ago
56 lines (55 loc) · 1.42 KB

Code

Blame
Skip to content
rickylambert.txt
Repository navigation
Code
Issues
Pull requests
1
 (1)
Actions
Projects
Commit 50042e4
rickyplambert-seed
rickyplambert-seed
authored
on Aug 13
‎.github/workflows/python-package-conda.yml‎
Original file line number	Diff line number	Diff line change
@@ -0,0 +1,34 @@
name: Python Package using Conda
on: [push]
jobs:
  build-linux:
    runs-on: ubuntu-latest
    strategy:
      max-parallel: 5
    steps:
    - uses: actions/checkout@v4
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: '3.10'
    - name: Add conda to system path
      run: |
        # $CONDA is an environment variable pointing to the root of the miniconda directory
        echo $CONDA/bin >> $GITHUB_PATH
    - name: Install dependencies
      run: |
        conda env update --file environment.yml --name base
    - name: Lint with flake8
      run: |
        conda install flake8
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Test with pytest
      run: |
        conda install pytest
        pytest
0 commit comments
Comments
0
 (0)
Comment
You're not receiving notifications from this thread.
