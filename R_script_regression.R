setwd('/Users/rpindale/Documents/DS5100/ds5100_prog_for_ds_jv/')


data <- read.csv('happy_and_COVID.csv')
head(data)
attach(data)


diff_fit<-lm(Ladder.score_diff ~ Logged.GDP.per.capita_diff + 
     Social.support_diff + Healthy.life.expectancy_diff + 
     Freedom.to.make.life.choices_diff + Generosity_diff + Perceptions.of.corruption_diff +
       COVID.19.deaths.per.100.000.population.in.2020)


summary(diff_fit)



lin_reg_covid_20<-lm(X20_Ladder.score ~ X20_Logged.GDP.per.capita + 
                       X20_Social.support + X20_Healthy.life.expectancy + 
               X20_Freedom.to.make.life.choices + X20_Generosity + X20_Perceptions.of.corruption 
               + X20_Ladder.score.in.Dystopia + X20_Explained.by..Log.GDP.per.capita +
                 X20_Explained.by..Social.support + X20_Explained.by..Healthy.life.expectancy +
                 X20_Explained.by..Freedom.to.make.life.choices + X20_Explained.by..Generosity + 
                 X20_Explained.by..Perceptions.of.corruption + X20_Dystopia...residual +
                 COVID.19.deaths.per.100.000.population.in.2020)


summary(lin_reg_covid_20)



lin_reg_covid_21<-lm(X21_Ladder.score ~ X21_Logged.GDP.per.capita + 
                       X21_Social.support + X21_Healthy.life.expectancy + 
                       X21_Freedom.to.make.life.choices + X21_Generosity + X21_Perceptions.of.corruption 
                     + X21_Ladder.score.in.Dystopia + X21_Explained.by..Log.GDP.per.capita +
                       X21_Explained.by..Social.support + X21_Explained.by..Healthy.life.expectancy +
                       X21_Explained.by..Freedom.to.make.life.choices + X21_Explained.by..Generosity + 
                       X21_Explained.by..Perceptions.of.corruption + X21_Dystopia...residual)


summary(lin_reg_covid_21)






lin_reg_covid_20_2<-lm(X20_Ladder.score ~ X20_Logged.GDP.per.capita + 
                       X20_Social.support + X20_Healthy.life.expectancy + 
                       X20_Freedom.to.make.life.choices + X20_Generosity + X20_Perceptions.of.corruption + 
                       COVID.19.deaths.per.100.000.population.in.2020)


summary(lin_reg_covid_20_2)



lin_reg_covid_21_2<-lm(X21_Ladder.score ~ X21_Logged.GDP.per.capita + 
                         X21_Social.support + X21_Healthy.life.expectancy + 
                         X21_Freedom.to.make.life.choices + X21_Generosity + X21_Perceptions.of.corruption + 
                         COVID.19.deaths.per.100.000.population.in.2020
                         )


summary(lin_reg_covid_21_2)






hist(Ladder.score_diff, breaks=20)
hist(Logged.GDP.per.capita_diff, breaks=20)
hist(Social.support_diff, breaks=20)
hist(Healthy.life.expectancy_diff, breaks=20)
hist(Freedom.to.make.life.choices_diff, breaks=20)
hist(Generosity_diff, breaks=20)
hist(Perceptions.of.corruption_diff, breaks=20)
