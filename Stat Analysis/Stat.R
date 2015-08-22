## Load in to data frame
setwd('C:/Users/jayakumara/Desktop/Temp')
d.f <- read.csv(file = "filtered.csv", head = TRUE, sep = ",")

Salary <- d.f$salary
hist(Salary)


logsal = log(d.f$salary)
plot(density(Salary, kernel = "gaussian", adjust=1, bw="SJ"))
# densityPlot( ~ salary, data=d.f, bw="SJ", adjust=1, kernel="gaussian")
plot(density(log(d.f$salary)))
plot(density(logsal, kernel = "gaussian", adjust=1, bw="SJ"))

qqnorm(d.f$salary, main = 'Normal Q-Q Plot (Salary)')
qqnorm(log(d.f$salary), main = 'Normal Q-Q Plot (Logsal)')

head(d.f)
logsal = log(d.f$salary)

regmodel = lm(logsal ~ experience+FG+MP+PTS+G+TWOP+THREEP+FT+TRB+PF+TOV, data = d.f)
regmodel = lm(cbind(duration, companyname, title) ~ timetocommute + numconnections + pastexperience + 
                degreescore + schoolscore + overallrating + culture + leadership + 
                compensation + career + worklife + recommend + overallpast + 
                culturepast + leadershippast + compensationpast + careerpast + 
                worklifepast + recommendpast + overallfactor + culturefactor + 
                leadershipfactor + compensationfactor + careerfactor + worklifefactor + recommendfactor, data = d.f)
summary(regmodel)

coefficient = coefficients(regmodel)
coefficient

confint.default(regmodel)
