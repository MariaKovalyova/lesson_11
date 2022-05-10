import os

from flask import Flask, render_template, request

from utils import *

project_root = os.path.dirname(__file__) # без этого не работает
template_path = os.path.join(project_root, './')

app = Flask(__name__, template_folder=template_path)


@app.route("/")
def list_page():
    return render_template('list.html', persons=load_candidates_from_sjson())


@app.route("/candidate/<int:candidate_id>")
def card_page(candidate_id):
    return render_template('card.html', person=get_candidate(candidate_id))


@app.route("/skill/<skill_name>")
def skill_page(skill_name):
    persons, count = get_candidates_by_skill(skill_name)
    return render_template('skill.html', persons=persons, count=count, skill=skill_name)


@app.route("/search/<candidate_name>")
def search_page(candidate_name):
    persons, count = get_dandidates_by_name(candidate_name)
    return render_template('search.html', persons=persons, count=count, name=candidate_name)


app.run()
