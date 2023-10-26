# 언어데이터과학 (2023학년도 2학기, 서울대학교 언어학과)

## 개요

+ 강좌명: 언어데이터과학
+ 강좌번호: M1246.001400 (001)
+ 교수자: 박수민 (mam3b@snu.ac.kr)
+ 부교재: *[The Open Handbook of Linguistic Data Management](https://direct.mit.edu/books/oa-edited-volume/5244/The-Open-Handbook-of-Linguistic-Data-Management)*
+ 선수과목: [컴퓨터의 개념 및 실습], [언어와 컴퓨터]

## 일정

|회차|날짜|제목|슬라이드|실습|자료|
|--|--|--|--|--|--|
|1강|2023-09-04(월)|강의 소개: 오리엔테이션|||
|2강|2023-09-06(수)|환경 설정: git|[[2강](./slides/02-20230906.pdf)]||
||2023-09-06(수)|[숙제00] 수강생 배경 조사||||
||2023-09-08(금)|[숙제01] git 설치 인증||||
|3강|2023-09-11(월)|Linux 기초|[[3강](./slides/03-202309011.pdf)]|[[grep 연습](./notes/03-20230911.MD)]|[[Apicius](https://www.gutenberg.org/ebooks/29728)]|
|4강|2023-09-13(수)|AWK 기초|[[4강](./slides/04-20230913.pdf)]|[[awk 기초](./notes/04-20230913.MD)]|
||2023-09-15(금)|[숙제02] Linux 및 AWK 연습||[[과제 설명](./hw/hw02/hw02-instruction.pdf)]||
|5강|2023-09-18(월)|데이터과학 (1): 데이터의 정의, 언어데이터의 범위, 데이터의 네 가지 범주, 기술통계량|[[5강](./slides/05-20230918.pdf)]||
|6강|2023-09-20(수)|데이터과학 (2): numpy|[[6강](./slides/06-20230920.pdf)]|[[노트북: 기술통계량](./notes/06-20230920-descriptive-statistics.ipynb)] [[노트북: numpy](./notes/06-20230920-numpy-arrays.ipynb)]|
||2023-09-22(금)|[숙제03] numpy 연습||[[bmi.py](./hw/hw03/bmi.py)]||
|7강|2023-09-25(월)|데이터과학 (3): 데이터 탐색 및 시각화|[[7강](./slides/07-20230925.pdf)]|[[노트북: pandas](./notes/07-20230925-pandas-dataframe.ipynb)] [[노트북: seaborn](./notes/07-20230925-visualization.ipynb)]|[[F0](./data/vowel/all-f0.csv)] [[F0-VOT](./data/vowel/women-f0-vot.csv)]|
|8강|2023-09-27(수)|데이터과학 (4): 다양한 빈도 개념|[[8강](./slides/08-20230927.pdf)][[추가](https://github.com/suparklingmin/news-title-gender/blob/main/slides.pdf)]||[[news-title-gender](https://github.com/suparklingmin/news-title-gender)]|
||2023-10-04(수)|[숙제04] 논문 요약: 국어 정보화의 방향|||[[국어 정보화의 방향](https://www.korean.go.kr/nkview/nklife/2015_2/25_0205.pdf)]|
|9강|2023-10-04(수)|텍스트 처리 (1): 문자 인코딩, 한글과 유니코드|[[9강](./slides/09-20231004.pdf)]||
||2023-10-06(금)|[숙제05] Word Cloud||[[노트북: wordcloud](https://github.com/suparklingmin/LingDataSci2023/blob/main/hw/hw05/hw05-word-cloud.ipynb)]||
||2023-10-06(금)|[숙제06] 9주차 발표 논문 선정||||
|10강|2023-10-11(수)|텍스트 처리 (2): 옛한글, 한문|||
||2023-10-13(금)|[숙제07] 모두의 말뭉치 사이트 가입 인증||||
|11강|2023-10-16(월)|데이터프레임 처리: Naver Sentiment Movie Corpus, pandas||[[노트북: konlpy](https://github.com/suparklingmin/LingDataSci2023/blob/main/notes/11-20231016-konlpy-morphological-analysis.ipynb)] [[노트북: wordcloud & nsmc](https://github.com/suparklingmin/LingDataSci2023/blob/main/notes/11-20231016-wordcloud-nsmc.ipynb)]|[[Naver sentiment movie corpus](https://github.com/e9t/nsmc)]|
|12강|2023-10-18(수)|JSON 파일 처리: 모두의 말뭉치 (1)||[[노트북: 대용량 파일 처리](https://github.com/suparklingmin/LingDataSci2023/blob/main/notes/12-20231018-preprocessing-modified.ipynb)]|[[모두의 말뭉치](https://corpus.korean.go.kr)]|
||2023-10-20(금)|[숙제08] pandas 연습||[[노트북: wordcloud revisited](https://github.com/suparklingmin/LingDataSci2023/blob/main/hw/hw08/hw08-nsmc-wordcloud.ipynb)]||
||2023-10-20(금)|[숙제09] 언어데이터 관리 사례 조사||[[발표 자료 예시](https://github.com/suparklingmin/LingDataSci2023/blob/main/hw/hw09/38-presentation.pdf)]||
|13강|2023-10-23(월)|JSON 파일 처리: 모두의 말뭉치 (2)||[[노트북: 데이터프레임 구축](https://github.com/suparklingmin/LingDataSci2023/blob/main/notes/12-20231018-counting-wanjeon.ipynb)]|[[모두의 말뭉치](https://corpus.korean.go.kr)]|
|14강|2023-10-25(수)|JSON 파일 처리: 모두의 말뭉치 (3)||[[노트북: 데이터프레임 병합](https://github.com/suparklingmin/LingDataSci2023/blob/main/notes/12-20231018-analyzing-wanjeon.ipynb)]|[[모두의 말뭉치](https://corpus.korean.go.kr)]|
|15강|2023-10-30(월)|언어데이터 관리 사례 발표(논문 발제 및 퀴즈) (1)|||
|16강|2023-11-01(수)|언어데이터 관리 사례 발표(논문 발제 및 퀴즈) (2)|||
||2023-10-27(금)|[숙제10] 언어데이터 관리 사례 퀴즈||||
||2023-10-27(금)|[숙제11] 개인 프로젝트 주제 선정||[[연구계획서 예시](https://github.com/suparklingmin/LingDataSci2023/blob/main/project/docs/proposal.pdf)]||
||2023-11-03(금)|[숙제12] 강의 평가 인증||||
|17강|2023-11-06(월)|코퍼스 구축 및 관리|||
|18강|2023-11-08(수)|코퍼스 공개 및 인용|||
||2023-11-10(금)|[숙제13] 개인 프로젝트 중간발표문||||
|19강|2023-11-13(월)|개인 프로젝트 중간발표 (1)|||
|20강|2023-11-15(수)|개인 프로젝트 중간발표 (2)|||
||2023-11-17(금)|[숙제14] 코퍼스 기술(description)||||
|21강|2023-11-20(월)|기계학습 (1): 지도학습, 훈련집합-실험집합 분할, 학습 결과 평가|||
|22강|2023-11-22(수)|기계학습 (2): sklearn 실습|||
|23강|2023-11-27(월)|워드 임베딩 (1): 정보 검색, TF-IDF|||
|24강|2023-11-29(수)|워드 임베딩 (2): 분포 가설, word2vec, gensim 실습|||
||2023-12-01(금)|[숙제15] 개인 프로젝트 최종발표문||||
|25강|2023-12-04(월)|개인 프로젝트 최종발표 (1)|||
|26강|2023-12-06(수)|개인 프로젝트 최종발표 (2)|||
||2023-12-18(월)|[기말] 개인 프로젝트 보고서 완성본 제출||||
