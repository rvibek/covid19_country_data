# Pull COVID19 country data

Git Action to fetch JHU data. The action runs as a cronjob at 2200 hours every day.


```
name: Configure
on:
 push:
  branches: main
 schedule:
    - cron: "0 21 * * *"

jobs:
 # python installtion
  install-python:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.8"]

    steps:
      - uses: actions/checkout@v2
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v2
        with:
          python-version: ${{ matrix.python-version }}


        
      - name: cml
        env:
          repo_token: ${{ secrets.GITHUB_TOKEN }}

        run: |
          
          pip install -r requirements.txt --upgrade pip
          python3 runtest.py
          
          # cat result.txt >> tmpresult.txt

          python3 scrap_jhu.py "Switzerland"
          python3 scrap_jhu.py "Germany"
          python3 scrap_jhu.py "Denmark"
          python3 scrap_jhu.py "India"
          python3 scrap_jhu.py "Nepal"
          

          
      - name: Commit files
        id: commit
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "github-actions"
          git add --all
          if [-z "$(git status --porcelain)"]; then
             echo "::set-output name=push::false"
          else
            git commit -m "Add changes" -a
            echo "::set-output name=push::true"
          fi
        shell: bash
    
      - name: Push changes
        if: steps.commit.outputs.push == 'true'
        uses: ad-m/github-push-action@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          

```
