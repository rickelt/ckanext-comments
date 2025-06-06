import ckan.plugins as plugins
import ckan.plugins.toolkit as tk

import ckanext.comments.helpers as helpers
import ckanext.comments.logic.action as action
import ckanext.comments.logic.auth as auth
import ckanext.comments.logic.validators as validators

from ckanext.comments import blueprint

try:
    config_declarations = tk.blanket.config_declarations
except AttributeError:
    config_declarations = lambda cls: cls


@config_declarations
class CommentsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IAuthFunctions)
    plugins.implements(plugins.IActions)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IValidators)
    plugins.implements(plugins.IBlueprint)

    # IConfigurer

    def update_config(self, config_):
        tk.add_template_directory(config_, "templates")
        tk.add_public_directory(config_, "public")
        tk.add_resource("assets", "comments")

    # IAuthFunctions

    def get_auth_functions(self):
        return auth.get_auth_functions()

    # IActions

    def get_actions(self):
        return action.get_actions()

    # ITemplateHelpers

    def get_helpers(self):
        return helpers.get_helpers()

    # IValidators

    def get_validators(self):
        return validators.get_validators()

    # IBLueprint

    def get_blueprint(self):
        return blueprint.get_blueprints()
