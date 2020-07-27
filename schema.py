import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db_session, Program, Section, Activity, Answer, ProgramSectionMapping, SectionActivityMapping


class ProgramType(SQLAlchemyObjectType):
    class Meta:
        model = Program
        interfaces = (relay.Node, )


class ProgramSectionMappingType(SQLAlchemyObjectType):
    class Meta:
        model = ProgramSectionMapping

        interfaces = (relay.Node, )


class SectionType(SQLAlchemyObjectType):
    class Meta:
        model = Section
        interfaces = (relay.Node, )


class SectionActivityMappingType(SQLAlchemyObjectType):
    class Meta:
        model = SectionActivityMapping
        interfaces = (relay.Node, )


class ActivityType(SQLAlchemyObjectType):
    class Meta:
        model = Activity
        interfaces = (relay.Node, )


class AnswerType(SQLAlchemyObjectType):
    class Meta:
        model = Answer
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    section = graphene.List(
        SectionType, 
        section_id=graphene.Argument(type=graphene.String, required=False),
        program_id=graphene.Argument(type=graphene.String, required=False)
    )

    all_programs = SQLAlchemyConnectionField(ProgramType.connection)
    all_sections = SQLAlchemyConnectionField(SectionType.connection)
    all_activities = SQLAlchemyConnectionField(ActivityType.connection)
    all_answers = SQLAlchemyConnectionField(AnswerType.connection)

    def resolve_section(parent, info, section_id=None, program_id=None):
        program_query = ProgramType.get_query(info=info)
        section_query = SectionType.get_query(info=info)
        if section_id:
            section_query = section_query.filter(Section.section_id==section_id)
            print(section_query) 
        return section_query.first()

schema = graphene.Schema(query=Query, types=[ProgramType, SectionType, ActivityType, AnswerType])
