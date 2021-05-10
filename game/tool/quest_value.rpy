# Stage

# quest_stages: is the list of all existing Stage tasks.
# it is used to keep all information about all Stages

# current_quest_stages: are the Stage currently active,
# contains only the data strictly necessary for proper operation
# after their completion they are replaced with the next one

# Task
# current_task_stages is identical to this_current, 
# except that after completion they are not replaced by the next one, but eliminated. 
# The idea is that the Tasks are not within the "Stage" and therefore have no subsequent internships.

# Quest
# the Quest is a list of Stages that follow each other according to their order
# quests and quests_levels are synchronized, meaning they will always have the same elements

# quests_levels: must not have elements at the beginning. what is it for? to know which number of this has arrived at an internship
# quest_stages is similar to quest_stages and contains information about internships

default quests_levels = {}
default current_quest_stages = {}
default current_task_stages = {}

# TODO: to be included in the documentation
# if you need a description of the quest that true over time this dictionary seemed to me the best way to do it
default quests_descriptions = {}

define quests = {
    "main"     :   Quest(id = "main", title = _("Main Quest"), bg="quest main", stages_id = ["main_introD"], development = True),
}
define quest_stages = {
    # Main Quest
    "main_introD"                   :   Stage(idQuestOrTask = "main", bg="quest main", title = _("The postit"), description = _("[emy] didn't want to go into detail about what happened yesterday. The only one who could tell me more is [mia]."), label_start="main_startstage"),
    # public transport Task
    "subscribe_public_transport"    :   Stage(idQuestOrTask = "subscribe_public_transport", title = _("Subscribe to public transport")),
}
