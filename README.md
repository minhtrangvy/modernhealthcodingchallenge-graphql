# Usage



# Assumptions
- Only GET requests are needed since this is a query library

# Sample Data
The sample data is created by running `inject_data.py`. This file is imported in `app.py` so leaving it in there will automatically inject dummy data. To not create dummy data, just comment out the import line in `app.py`.

Same data consists of:
- 4 Programs, 
- the number of Sections per Program is the same as suggested in the coding challenge description. The Sections are all unique (no Programs share sections).
- However, all Sections have *the same* 4 Activities: 2 HTML Content Activities and 2 Question Activities. 
- There are 5 Answer dummy records. Each time `inject_data.py` is run, it randomly gives assigns 1 to 5 answers to the 2 Question Activities.

To keep track of the relationship between Programs and Sections, a ProgramSectionMapping table exists. This is also the reason that Programs have their own program_id and Sections have their own section_id (in the case that Program can share the same Sections).  

# Useful Queries
## Get all programs
```
{
  allPrograms {
    edges {
      node {
        programId,
        name,
        description
      }
    }
  }
}
```
```
{
  "data": {
    "allPrograms": {
      "edges": [
        {
          "node": {
            "programId": "d814b582727c4564bf16aefb058ff5c0",
            "name": "New Parenting",
            "description": "Learn to parent yourself"
          }
        },
        {
          "node": {
            "programId": "dd9fd23749e244498affe0730d83ec38",
            "name": "Leadership Development Program",
            "description": "Training to be a better leader"
          }
        },
        {
          "node": {
            "programId": "ae4861dd997f49fe910a1477a14bac63",
            "name": "Mindful Communication",
            "description": "Communicate effectively"
          }
        },
        {
          "node": {
            "programId": "670df3067af54f7bb9c1ec4d631e1e3d",
            "name": "Cognitive Behavioral Therapy",
            "description": "Take a theoretical approach"
          }
        }
      ]
    }
  }
}
```

## Query details of a single program

## Get all Sections for a Program, ordered

## Get section details for a given section

## Get all Activities

## Get all Activities given a Section

## Get details of an Activity

## Get all answers for a Questions Activity