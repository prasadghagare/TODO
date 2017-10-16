import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    pass

class RunConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'run.db')

class TestConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')

class FuncTestConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'func_test.db')

config = {
    'runtime' : RunConfig,
    'test' : TestConfig,
    'default': RunConfig,
    'func_test': FuncTestConfig
}
