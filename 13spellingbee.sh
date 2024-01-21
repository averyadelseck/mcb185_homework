echo: "For word count"

gunzip -c dictionary.gz | grep -v "[bdefghjklmpqstuvwxy]" | grep "r" | grep ".....*" | wc -l

echo: "For actual words"

gunzip -c dictionary.gz | grep -v "[bdefghjklmpqstuvwxy]" | grep "r" | grep ".....*"
