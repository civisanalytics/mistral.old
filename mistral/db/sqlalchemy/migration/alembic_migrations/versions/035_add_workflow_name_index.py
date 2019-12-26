"""Add workflow_name index in action_executions_v2 table

Revision ID: 035
Revises: 034
Create Date: 2019-12-26 17:21:14.975474

"""

# revision identifiers, used by Alembic.
revision = '035'
down_revision = '034'

from alembic import op


def upgrade():
    op.create_index(
        'action_executions_v2_workflow_name',
        'action_executions_v2',
        ['workflow_name'],
        unique=False
    )
