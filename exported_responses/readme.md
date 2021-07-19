# Description of files

## event_194_survey_48_2021-07-14-1534-cest.csv
* [post-workshop-survey-2020](https://indico.neic.no/event/194/manage/surveys/48/)
* submission from 18 June 2021 to 13 Jul 2021 (at the time of esporting this file at 2021-07-14-1534-cest)
* Workshops covered: Trondheim, Oct 2019 - Online, Nov 2020
* 74 submissions

## event_109_survey_24.csv
* [post-workshop-survey-2019](https://indico.neic.no/event/109/manage/surveys/24/) 4 Nov
* submission from 11 Nov 2019 to 27 Jan 2020
* Workshops covered: Stockholm, March 2019 - Aalborg, June 2019
* 45 submissions

## event_80_survey_13.csv
* [post-workshop-survey-2019](https://indico.neic.no/event/80/manage/surveys/13/) 12 Apr
* submission from 12 Apr 2019 to 24 Apr 2019
* Workshops covered: Kiruna, Nov 2018 - Tautu, Apr 2019
* 36 submissions

## event_39_survey_5.csv
* [post-workshop-survey-2018](https://indico.neic.no/event/39/manage/surveys/5/) 31 Oct
* submission from 8 Nov 2018 to 12 Dec 2020
* Workshops covered: Lund, May 2018 - Espoo, May 2018
* 38 submissions

# Differences in questions and choice alternatives
Except for the first question of each survey "which workshop did you attend?", the surveys have mostly the same questions and choice alternatives. However, the followings are different and needs some attentions when it comes to processing.

## Sectioning 
194-48 is divided into 2 sections of "Background information" and "Impact of the workshop", while the other 3 survey responses has only "Post-workshop survey" section

## Questions
* 194-48 has "Participation style" question (e.g. "individual learner", "individual helper / exercise leader (online)" etc.)
* In 39-5, "Which tools/services have you started using as a result of attending the workshop?" while in the other 3, "Which tools/services **/workflows** have you started using as a result of attending the workshop?" ("/workflows" is added)
* 109-24 and 194-48 has "Would you recommend your colleagues to attend a CodeRefinery workshop?" question with 5 options 

## Choice alternatives
* 109-24 and 194-48 has "None of the above" option for "Would you judge your code to be better reusable/reproducible/modular/documented as a result of attending the workshop?" question
* For "Which tools/services have you started using as a result of attending the workshop?":
    * in 39-5, choice alternatives ;
        - are in different order from the other 3, and
        - are fewer than the other 3
        - has "CMake" alternative that the other 3 do not have. (In 109-24 and 194-48, there is "Workflow management tools (e.g. Snakemake)" , while in 80-13 there is "workflow systems (e.g. Snakemake)".)
    * In 39-5 and 80-13, there is "Integrated development environments" alternative which is not in the other 2.

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