# Description of files


## 2019-c-2020.csv

- <https://indico.neic.no/event/194/manage/surveys/48/>
- Submission from 18 June 2021 to 19 Jul 2021
- Workshops covered: Trondheim, Oct 2019 - Online, Nov 2020


## 2019-b.csv

- <https://indico.neic.no/event/109/manage/surveys/24/>
- Submission from 11 Nov 2019 to 27 Jan 2020
- Workshops covered: Stockholm, March 2019 - Aalborg, June 2019


## 2019-a.csv

- <https://indico.neic.no/event/80/manage/surveys/13/>
- Submission from 12 Apr 2019 to 24 Apr 2019
- Workshops covered: Kiruna, Nov 2018 - Tautu, Apr 2019


## 2018.csv

- <https://indico.neic.no/event/39/manage/surveys/5/>
- Submissions from 8 Nov 2018 to 12 Dec 2020
- Workshops covered: Lund, May 2018 - Espoo, May 2018


# Differences in questions and choice alternatives

Except for the first question of each survey "which workshop did you attend?",
the surveys have mostly the same questions and choice alternatives. However,
the followings are different and needs some attentions when it comes to
processing.

## Sectioning 
2019-c-2020.csv is divided into 2 sections of "Background information" and "Impact of the workshop", while the other 3 survey responses has only "Post-workshop survey" section

## Questions
* 2019-c-2020.csv has "Participation style" question (e.g. "individual learner", "individual helper / exercise leader (online)" etc.)
* In 2018.csv, the 4 questions starting with "Which tools/services ..." don't have "**/workflows**" after "services", while in the other 3 surveys they have. 
* 2019-b.csv and 2019-c-2020.csv has "Would you recommend your colleagues to attend a CodeRefinery workshop?" question with 5 options 

## Choice alternatives
* 2019-b.csv and 2019-c-2020.csv has "None of the above" option for "Would you judge your code to be better reusable/reproducible/modular/documented as a result of attending the workshop?" question
* For the 4 questions starting with "Which tools/services ...":
    * in 2018.csv, choice alternatives ;
        - are in different order from the other 3, and
        - are fewer than the other 3
        - has "CMake" alternative that the other 3 do not have. (In 2019-b.csv and 2019-c-2020.csv, there is "Workflow management tools (e.g. Snakemake)" , while in 2019-a.csv there is "workflow systems (e.g. Snakemake)".)
    * In 2018.csv and 2019-a.csv, there is "Integrated development environments" alternative which is not in the other 2.

## Difference from Typeform-based survey responses
"workshop-followup-survey-201*_processed.csv" files are formatted in a different way from the exported survey responses from Indico. It seems that the survey in Typeform had fewer questions asked as well.

Major differences are as follows:
* In typeform-based survey responses, questions and responses about 
    *  use of introduced tools are shown as
        * tool as a column header
        * choice alternative from "I don't use this tool", "I started using this tool", "I'm using this tool better than before", "I'm using this tool in the same way as before" as data
    *  effects in coding practice are shown as
        * effect type (e.g. "reusable", "reproducible", "modular" and "better documented" as well as "easier collaboration" and "introduction of tnew tools/practices") as column header
        * 1 or 0 as data
* In Indico survey responses, 
    * each "section:question" is shown as a column header, and
    * all the chosen alternatives are shown with ";" separation as written in the survey (i.e. "yes" as "yes" but not as "1")
