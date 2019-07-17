opencv_traincascade.exe -data xml -vec pos.vec -bg neg.txt -numPos 120 -numNeg 278 -numStages 15 -w 30 -h 30 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -weightTrimRate 0.95 -featureType HAAR
pause