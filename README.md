# 🎵 Kpop-lyric-datasets

There are json-formated datas of 25696 k-pop songs, which was from **Melon's Monthly Chart Ranking 100 (2000 ~ 2023 Oct.)**. <br>
Also providing python utilities for data handling. <br> <br>
*I DO NOT claim any ownership of this dataset, All copyrights belong to the authors, of each song.* <br>
*You can freely use this dataset on RESEARCH PURPOSE, but if you want to use COMMERCIALLY this dataset, You should Talk with Lyricists, Artists, Composers, etc.*
<br> <br>
## 🤔 1. How to Use
Clone this repository into your workspace.
```Git
git clone https://github.com/EX3exp/Kpop-lyric-datasets.git
```

## 📖 2. Usage
### 🤔 A. Getting 2023's whole data into Dictionary
```Python
from utils import data_parser
your_dict = data_parser.get_dict(2023)
```

### 🤔 B. Getting whole data from 2010 to 2022, into Dataframe(Pandas)
```Python
from utils import data_parser
your_dataframe = data_parser.get_df(2010, 2022)
```

## 📖 3. Structure
🔽 Introducing data's structure with `melon-monthly_2023-07_16.json` - 🐇 *(Attention - New Jeans).*
### 🔖 0. Path of jsons
```Bash
melon\monthly-chart\melon-<year>\melon-<year>-<month>\melon-monthly_<year>-<month>_<chart rank>.json
```
### 🔖 1. info
Metadata of this song. 
```json
{
    "info": [
        {
            "year": 2023,
            "month": 7,
            "rank": 16,
            "type": "월별차트",
            "website": "Melon"
        },
        ""
    ],
```
### 🔖 2. song_id
Id of this song, which is in **Melon Database**.
```json
"song_id": "35454425",
```
### 🔖 3. song_name
Name of this song.
```json
"song_name": "Attention",
```
### 🔖 4. album
Album's name.
```json
"album": "NewJeans 1st EP 'New Jeans'",
```
### 🔖 5. release_date
Song's released date. 
```json
"release_date": "2022.08.01",
```
### 🔖 6. artist
Artist of this song.
```json
"artist": "NewJeans",
```
### 🔖 7. genre
Genre of this song, which was specified in Melon.
```json
"genre": "댄스",
```
### 🔖 8. lyric_writer
Lyricist of this song.
```json
"lyric_writer": "Gigi",
```
### 🔖 9. composer
Composer of this song.
```json
"composer": "Duckbay (Cosmos Studios Stockholm)",
```
### 🔖 10. arranger
Arranger of this song.
```json
"arranger": "다니엘(DANIELLE)",
```
### 🔖 11. lyrics
Lyrics are separated per line.
#### 1) row_num
Number of lyrics' rows.
```json
 "lyrics": {
    "row_num": 79,
```
#### 2) lines
Whole lyrics of this song.
```json
    "lines": [
            "You and me",
            "내 맘이 보이지",
            "한참을 쳐다봐",
            "가까이 다가가",
            "You see",
            "You see, ey ey ey ey",
            "",
            "One, two, three",
            "용기가 생겼지",
            "이미 아는 네 눈치",
            "고개를 돌려 천천히",
            "여기",
            "You see",
            "여기 보이니",
            "",
            "Looking for attention 너야겠어",
            "확실하게 나로 만들겠어",
            "Stop, eyyy",
            "Drop the question",
            "Drop the, drop the question",
            "Want attention",
            "Wanna want attention",
            "",
            "You give me butterflies you know",
            "내 맘은 온통 paradise",
            "꿈에서 깨워주지 마",
            "",
            "You got me looking for attention",
            "You got me looking for attention",
            "가끔은 정말",
            "헷갈리지만",
            "분명한 건",
            "Got me looking for attention",
            "",
            "널 우연히 마주친 척할래",
            "못 본 척 지나갈래",
            "You’re so fine",
            "Gotta gotta get to know ya",
            "나와 나와 걸어가 줘",
            "",
            "지금 돌아서면",
            "I need ya, need ya, need ya",
            "To look at me back",
            "Hey 다 들켰었나",
            "널 보면 하트가 튀어나와",
            "",
            "난 사탕을 찾는 baby (baby)",
            "내 맘은 설레이지",
            "Eyyy, drop the question",
            "Drop the, drop the question",
            "Want attention",
            "Wanna want attention",
            "",
            "You give me butterflies you know",
            "내 맘은 온통 paradise",
            "꿈에서 깨워주지 마",
            "",
            "You got me looking for attention",
            "You got me looking for attention",
            "가끔은 정말",
            "헷갈리지만",
            "분명한 건",
            "Got me looking for attention",
            "",
            "You got me looking for attention",
            "You got me looking for attention",
            "가끔은 정말",
            "헷갈리지만",
            "분명한 건",
            "Got me looking for attention",
            "",
            "A T T E N T I on",
            "Attention is what I want",
            "A T T E N T I on",
            "Attention is what I want",
            "A T T E N T I on",
            "Attention is what I want",
            "A T T E N T I on",
            "You got me looking for attention"
        ]
```
### 🔖 Whole Json 🐇
```json
{
    "info": [
        {
            "year": 2023,
            "month": 7,
            "rank": 16,
            "type": "월별차트",
            "website": "Melon"
        },
        ""
    ],
    "song_id": "35454425",
    "song_name": "Attention",
    "album": "NewJeans 1st EP 'New Jeans'",
    "release_date": "2022.08.01",
    "artist": "NewJeans",
    "genre": "댄스",
    "lyric_writer": "Gigi",
    "composer": "Duckbay (Cosmos Studios Stockholm)",
    "arranger": "다니엘(DANIELLE)",
    "lyrics": {
        "row_num": 79,
        "lines": [
            "You and me",
            "내 맘이 보이지",
            "한참을 쳐다봐",
            "가까이 다가가",
            "You see",
            "You see, ey ey ey ey",
            "",
            "One, two, three",
            "(... etc.)"
        ]
    }
}
```
