from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField, FileSize, FileAllowed
from wtforms import StringField, TextAreaField, SelectMultipleField, SubmitField,FieldList,FormField
from flask_sqlalchemy import SQLAlchemy, session
from app.models import Tag
from app import db
from wtforms_sqlalchemy.fields import QuerySelectMultipleField




class IngredientForm(FlaskForm):
    ingredient = StringField(label="Recipe Ingredients!")

class DirectionForm(FlaskForm):
    direction = StringField(label="Recipe Directions!")

class AddRecipe(FlaskForm):
    def tag_collector():
        return db.session.query(Tag).all()
    recipe_name = StringField('Name your recipe.', description="Give a succent yet detailed name for your recipe")
    recipe_ingredients = FieldList(FormField(IngredientForm),min_entries=1)
    recipe_directions = FieldList(FormField(DirectionForm),min_entries=1)
    recipe_tags = QuerySelectMultipleField(query_factory=tag_collector)
    recipe_description = TextAreaField('Provide details about the recipe and why it should be made')
    file = FileField('File', validators=[
        FileAllowed([".jpeg",".png"]),
        FileRequired(message='a file must be included to submit')
    ])
    submit = SubmitField('Submit')

class UpdateRecipe(FlaskForm):
    def tag_collector():
        return db.session.query(Tag).all()

    recipe_name = StringField('Name your recipe.', description="Give a succent yet detailed name for your recipe")
    recipe_ingredients = FieldList(FormField(IngredientForm))
    recipe_directions = FieldList(FormField(DirectionForm))
    recipe_tags = QuerySelectMultipleField(query_factory=tag_collector)
    recipe_description = TextAreaField('Provide details about the recipe and why it should be made')
    file = FileField('File', validators=[
        FileAllowed([".jpeg",".png"])
    ])
    submit = SubmitField('Submit')



class AddTag(FlaskForm):
    tag_name = StringField('Tag name.', description='Short, single word tag name.')
    submit = SubmitField('Submit')