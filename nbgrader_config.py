c = get_config()

###############################################################################
# Begin additions by nbgrader quickstart
###############################################################################

# You only need this if you are running nbgrader on a shared
# server set up.
c.Exchange.course_id = "nbgrader-test-course"
c.Exchange.root = "/tmp/exchange"

# Update this list with other assignments you want
c.CourseDirectory.db_assignments = [dict(name="week1")]

# Change the students in this list with that actual students in
# your course
c.CourseDirectory.db_students = [
    dict(id="karen", first_name="Karen", last_name="Cranston"),
]

c.IncludeHeaderFooter.header = "source/header.ipynb"

###############################################################################
# End additions by nbgrader quickstart
###############################################################################

# Configuration file for nbgrader-generate-config.

#------------------------------------------------------------------------------
# Application(SingletonConfigurable) configuration
#------------------------------------------------------------------------------

## This is an application.

## The date format used by logging formatters for %(asctime)s
#c.Application.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#c.Application.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#c.Application.log_level = 30

#------------------------------------------------------------------------------
# JupyterApp(Application) configuration
#------------------------------------------------------------------------------

## Base class for Jupyter applications

## Answer yes to any prompts.
#c.JupyterApp.answer_yes = False

## Full path of a config file.
#c.JupyterApp.config_file = ''

## Specify a config file to load.
#c.JupyterApp.config_file_name = ''

## Generate default config file.
#c.JupyterApp.generate_config = False

#------------------------------------------------------------------------------
# NbGrader(JupyterApp) configuration
#------------------------------------------------------------------------------

## A base class for all the nbgrader apps.

## Name of the logfile to log to.
#c.NbGrader.logfile = '.nbgrader.log'

#------------------------------------------------------------------------------
# GenerateConfigApp(NbGrader) configuration
#------------------------------------------------------------------------------

## The name of the configuration file to generate.
#c.GenerateConfigApp.filename = 'nbgrader_config.py'

#------------------------------------------------------------------------------
# CourseDirectory(LoggingConfigurable) configuration
#------------------------------------------------------------------------------

## The assignment name. This MUST be specified, either by setting the config
#  option, passing an argument on the command line, or using the --assignment
#  option on the command line.
#c.CourseDirectory.assignment_id = ''

## The name of the directory that contains assignment submissions after they have
#  been autograded. This corresponds to the `nbgrader_step` variable in the
#  `directory_structure` config option.
#c.CourseDirectory.autograded_directory = 'autograded'

## A list of assignments that will be created in the database. Each item in the
#  list should be a dictionary with the following keys:
#  
#      - name
#      - duedate (optional)
#  
#  The values will be stored in the database. Please see the API documentation on
#  the `Assignment` database model for details on these fields.
#c.CourseDirectory.db_assignments = []

## A list of student that will be created in the database. Each item in the list
#  should be a dictionary with the following keys:
#  
#      - id
#      - first_name (optional)
#      - last_name (optional)
#      - email (optional)
#  
#  The values will be stored in the database. Please see the API documentation on
#  the `Student` database model for details on these fields.
#c.CourseDirectory.db_students = []

## URL to the database. Defaults to sqlite:///<root>/gradebook.db, where <root>
#  is another configurable variable.
#c.CourseDirectory.db_url = ''

## Format string for the directory structure that nbgrader works over during the
#  grading process. This MUST contain named keys for 'nbgrader_step',
#  'student_id', and 'assignment_id'. It SHOULD NOT contain a key for
#  'notebook_id', as this will be automatically joined with the rest of the path.
#c.CourseDirectory.directory_structure = '{nbgrader_step}/{student_id}/{assignment_id}'

## The name of the directory that contains assignment feedback after grading has
#  been completed. This corresponds to the `nbgrader_step` variable in the
#  `directory_structure` config option.
#c.CourseDirectory.feedback_directory = 'feedback'

## List of file names or file globs to be ignored when copying directories.
#c.CourseDirectory.ignore = ['.ipynb_checkpoints', '*.pyc', '__pycache__']

## File glob to match notebook names, excluding the '.ipynb' extension. This can
#  be changed to filter by notebook.
#c.CourseDirectory.notebook_id = '*'

## The name of the directory that contains the version of the assignment that
#  will be released to students. This corresponds to the `nbgrader_step` variable
#  in the `directory_structure` config option.
#c.CourseDirectory.release_directory = 'release'

## The root directory for the course files (that includes the `source`,
#  `release`, `submitted`, `autograded`, etc. directories). Defaults to the
#  current working directory.
#c.CourseDirectory.root = ''

## The name of the directory that contains the master/instructor version of
#  assignments. This corresponds to the `nbgrader_step` variable in the
#  `directory_structure` config option.
#c.CourseDirectory.source_directory = 'source'

## File glob to match student IDs. This can be changed to filter by student.
#  Note: this is always changed to '.' when running `nbgrader assign`, as the
#  assign step doesn't have any student ID associated with it.
#  
#  If the ID is purely numeric and you are passing it as a flag on the command
#  line, you will need to escape the quotes in order to have it detected as a
#  string, for example `--student=""12345""`. See:
#  
#      https://github.com/jupyter/nbgrader/issues/743
#  
#  for more details.
#c.CourseDirectory.student_id = '*'

## The name of the directory that contains assignments that have been submitted
#  by students for grading. This corresponds to the `nbgrader_step` variable in
#  the `directory_structure` config option.
#c.CourseDirectory.submitted_directory = 'submitted'
