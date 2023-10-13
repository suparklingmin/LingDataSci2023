BEGIN{
    RS="\r?\n\r?\n(\r?\n)+"
    FS="\r?\n\r?\n"
    OFS="\n"
}
/^\[[0-9]+\]/{
    # $1에서 영어 이름과 라틴어 이름 사이의 줄바꿈 문자를 없애기
    gsub("[ ]*\r?\n[ ]*", " - ", $1)

    # $2에서 줄바꿈 문자 없애기
    gsub("\r?\n", " ", $2)

    # $0(모든 필드)에서 각주 번호 없애기
    gsub(" _?\\[[0-9]+\\]_?", "", $1)
    gsub(" \\[[0-9]+\\]", "", $2)
    
    OUTPUTFILE = "data/apicius/recipes/" $1 ".txt"
    print $2 > OUTPUTFILE
}