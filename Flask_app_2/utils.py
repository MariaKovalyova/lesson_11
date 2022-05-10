from json import load

candidate_file = "candidates.json"


def load_candidates_from_sjson(path=candidate_file):
    with open(path, 'r', encoding="UTF=8") as file:
        return load(file)


def get_candidate(candidate_id):
    candidates_list = load_candidates_from_sjson(candidate_file)
    for candidate in candidates_list:
        if candidate.get("id") == candidate_id:
            return candidate


def get_dandidates_by_name(candidate_name):
    candidate_list = load_candidates_from_sjson()
    persons = []  # список подходящих кандидатов
    for person in candidate_list:
        if candidate_name.lower() in (person.get('name')).lower().split():
            persons.append(person)
    return persons, len(persons)


def get_candidates_by_skill(skill_name):
    candidate_list = load_candidates_from_sjson()
    persons = [] # список подходящих кандидатов
    for person in candidate_list:
        if skill_name.lower() in (person.get('skills')).lower():
            persons.append(person)
    return persons, len(persons)
