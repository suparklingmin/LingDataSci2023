# Linguistics and Data Science [hw02]
# Release date: 2023-10-08
# Due date: 2023-10-13 1:00 PM

BEGIN {
    RS="\r?\n\r?\n(\r?\n)+" # 줄바꿈 문자 세 개 이상의 연쇄
    FS="\r?\n(\r?\n)+" # 줄바꿈 문자 두 개 이상의 연쇄
    # DO SOMETHING HERE
    # DO SOMETHING HERE
}
/^\[[0-9]+\]/ {
    gsub("[ \n]\\[[0-9]+\\]", "", $0) # 각주 번호 제거
    gsub("_\\[[0-9]+\\]_", "", $0) # 라틴어 원문의 각주 번호 제거

    # DO SOMETHING HERE
    # DO SOMETHING HERE
    # DO SOMETHING HERE

    print $1, $2
}