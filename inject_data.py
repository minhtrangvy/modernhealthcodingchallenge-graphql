from util import * 
import random
from models import engine, db_session, Base, Program, Section, ProgramSectionMapping, ActivityEnum, Activity, SectionActivityMapping, Answer

Base.metadata.drop_all(engine)
Base.metadata.create_all(bind=engine)

db_session.query(Program).delete()
db_session.query(Section).delete()
db_session.query(Activity).delete()
db_session.query(Answer).delete()

# Fill the tables with some data

programs = {
    'leadership': {
        'name': 'Leadership Development Program',
        'program_id': '',
        'description': 'Training to be a better leader',
        'num_sections': 10
    },
    'cbt': {
        'name': 'Cognitive Behavioral Therapy',
        'program_id': '',
        'description': 'Take a theoretical approach',
        'num_sections': 8
    },
    'parenting': {
        'name': 'New Parenting',
        'program_id': '',
        'description': 'Learn to parent yourself',
        'num_sections': 4
    },
    'comm': {
        'name': 'Mindful Communication',
        'program_id': '',
        'description': 'Communicate effectively',
        'num_sections': 4
    }
}

activities_per_section = 5
num_activities_per_section = 4
activities = []

# activities: half html and half questsions
# answers: create 5, randomly assign x number of answers to quesetion activities

def add_and_commit(obj):
    db_session.add(obj)
    db_session.commit()

# Insert 5 answers to reuse among the Question activities
def insert_answer(i, activity_id):
    answer = Answer(answer="Option" + str(i), activity_id=activity_id)
    add_and_commit(answer)

# Insert 2 HTML Activities
def create_html_activities(activities):
    for k in range(2):
        activity_id = generate_random_uuid()
        html_activity = Activity(activity_id=activity_id, activity_type=ActivityEnum.HTML, description="blahblahblah")
        add_and_commit(html_activity)
        activities += [activity_id]

# Insert 2 Question Activities with 3 answers each
def create_question_and_activities_with_answers(activities):
    for l in range(2):
        activity_id = generate_random_uuid()
        qa_activity = Activity(activity_id=activity_id, activity_type=ActivityEnum.MULTIPLE_CHOICE, description="Question " + str(l))
        add_and_commit(qa_activity)
        activities += [activity_id]

        # insert a random number of answers for this question
        for k in range(random.randint(1,5)):
            insert_answer(k, activity_id)

def create_programs(programs):
    for prog in programs:
        program_id = generate_random_uuid()   
        program = Program(program_id=program_id, name=programs[prog]['name'], description=programs[prog]['description'])
        add_and_commit(program) 
        programs[prog]['program_id'] = program_id

def create_sections_for_programs(programs, activities):
    for prog in programs:
        for i in range(programs[prog]['num_sections']):
            section_id = generate_random_uuid()
            section_name = prog + " section " + str(i)
            section = Section(section_id=section_id, name=section_name, description=section_name, overview_image=section_name + ".png")
            add_and_commit(section)

            prog_section_mapping = ProgramSectionMapping(mapping_id=generate_random_uuid(), program_id=programs[prog]['program_id'], section_id=section_id, order_index=i+1)
            add_and_commit(prog_section_mapping)

            for activity_id in activities:
                section_activity_mapping = SectionActivityMapping(mapping_id=generate_random_uuid(), section_id=section_id, activity_id=activity_id)


create_html_activities(activities)
create_question_and_activities_with_answers(activities)
print(activities)
create_programs(programs)
print(programs)
create_sections_for_programs(programs, activities)

# def create_program_and_section_data(num_sections, program_short_name, program_full_name):
#     sections = []
#     for i in range(1,num_sections+1):
#         section_id = generate_random_uuid()
#         i_str = str(i)
#         section_name = program_short_name + " section " + i_str
#         current_section = Section(section_id=section_id, name=section_name, description=section_name, overview_image=section_name + ".png", order_index=i)
#         add_and_commit(current_section)
#         db_session.refresh(current_section)
#         for activity_id in activities:
#             current_section.activity = activity_id
#             db_session.commit()
#         sections += [current_section.section_id]

#     program_id = generate_random_uuid()
#     for section_id in sections:
#         program = Program(program_id=program_id, name=program_full_name, description="Training to be a better leader", section=section_id)
#         add_and_commit(program)

# create_program_and_section_data(10, "leadership", "Leadership Development Program")
# create_program_and_section_data(8, "cbt", "Cognitive Behavioral Therapy")
# create_program_and_section_data(4, "parenting", "New Parenting")
# create_program_and_section_data(4, "comm", "Mindful Communication")



def printAllRecords(table):
    records = db_session.query(table).all()
    for record in records:
        print(record.__dict__)

printAllRecords(Program)
printAllRecords(Section)
printAllRecords(Activity)
printAllRecords(Answer)