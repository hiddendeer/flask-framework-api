"""empty message

Revision ID: e52662b661d2
Revises: 
Create Date: 2023-12-14 15:41:34.145596

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e52662b661d2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dvadmin_system_dict',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sort', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('code', sa.String(length=50), nullable=True),
    sa.Column('code1', sa.String(length=50), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('code', sa.String(length=50), nullable=True),
    sa.Column('user_id', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('sys_user', schema=None) as batch_op:
        batch_op.drop_index('sys_user_company_id')
        batch_op.drop_index('sys_user_del_flag')
        batch_op.drop_index('sys_user_login_name')
        batch_op.drop_index('sys_user_office_id')
        batch_op.drop_index('sys_user_update_date')

    op.drop_table('sys_user')
    op.drop_table('sequence')
    op.drop_table('sys_role_menu')
    op.drop_table('sys_menu')
    op.drop_table('sys_user_friend')
    op.drop_table('sys_user_role')
    with op.batch_alter_table('sys_role', schema=None) as batch_op:
        batch_op.drop_index('sys_role_del_flag')
        batch_op.drop_index('sys_role_enname')

    op.drop_table('sys_role')
    with op.batch_alter_table('sys_log', schema=None) as batch_op:
        batch_op.drop_index('sys_log_create_by')
        batch_op.drop_index('sys_log_create_date')
        batch_op.drop_index('sys_log_request_uri')
        batch_op.drop_index('sys_log_type')

    op.drop_table('sys_log')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('mobile', sa.String(length=50), nullable=True))
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=255),
               type_=sa.String(length=50),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.String(length=50),
               type_=mysql.VARCHAR(collation='utf8mb4_general_ci', length=255),
               nullable=False)
        batch_op.drop_column('mobile')
        batch_op.drop_column('username')

    op.create_table('sys_log',
    sa.Column('id', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=64), nullable=False, comment='编号'),
    sa.Column('type', mysql.CHAR(charset='utf8mb3', collation='utf8mb3_bin', length=1), server_default=sa.text("'1'"), nullable=True, comment='日志类型'),
    sa.Column('title', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=255), nullable=True, comment='日志标题'),
    sa.Column('create_by', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=64), nullable=True, comment='创建者'),
    sa.Column('create_date', mysql.DATETIME(), nullable=True, comment='创建时间'),
    sa.Column('remote_addr', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=255), nullable=True, comment='操作IP地址'),
    sa.Column('user_agent', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=255), nullable=True, comment='用户代理'),
    sa.Column('request_uri', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=255), nullable=True, comment='请求URI'),
    sa.Column('method', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=5), nullable=True, comment='操作方式'),
    sa.Column('params', mysql.TEXT(charset='utf8mb3', collation='utf8mb3_bin'), nullable=True, comment='操作提交的数据'),
    sa.Column('exception', mysql.TEXT(charset='utf8mb3', collation='utf8mb3_bin'), nullable=True, comment='异常信息'),
    sa.PrimaryKeyConstraint('id'),
    comment='日志表',
    mysql_comment='日志表',
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    with op.batch_alter_table('sys_log', schema=None) as batch_op:
        batch_op.create_index('sys_log_type', ['type'], unique=False)
        batch_op.create_index('sys_log_request_uri', ['request_uri'], unique=False)
        batch_op.create_index('sys_log_create_date', ['create_date'], unique=False)
        batch_op.create_index('sys_log_create_by', ['create_by'], unique=False)

    op.create_table('sys_role',
    sa.Column('id', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=64), nullable=False, comment='编号'),
    sa.Column('office_id', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=64), nullable=True, comment='归属机构'),
    sa.Column('name', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=100), nullable=False, comment='角色名称'),
    sa.Column('enname', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=255), nullable=True, comment='英文名称'),
    sa.Column('role_type', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=255), nullable=True, comment='角色类型'),
    sa.Column('is_sys', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=64), nullable=True, comment='是否系统数据'),
    sa.Column('useable', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=64), nullable=True, comment='是否可用'),
    sa.Column('create_by', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=64), nullable=False, comment='创建者'),
    sa.Column('create_date', mysql.DATETIME(), nullable=False, comment='创建时间'),
    sa.Column('update_by', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=64), nullable=False, comment='更新者'),
    sa.Column('update_date', mysql.DATETIME(), nullable=False, comment='更新时间'),
    sa.Column('remarks', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=255), nullable=True, comment='备注信息'),
    sa.Column('del_flag', mysql.CHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=1), server_default=sa.text("'0'"), nullable=False, comment='删除标记'),
    sa.PrimaryKeyConstraint('id'),
    comment='角色表',
    mysql_comment='角色表',
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    with op.batch_alter_table('sys_role', schema=None) as batch_op:
        batch_op.create_index('sys_role_enname', ['enname'], unique=False)
        batch_op.create_index('sys_role_del_flag', ['del_flag'], unique=False)

    op.create_table('sys_user_role',
    sa.Column('user_id', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=64), nullable=False, comment='用户编号'),
    sa.Column('role_id', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=64), nullable=False, comment='角色编号'),
    sa.PrimaryKeyConstraint('user_id', 'role_id'),
    comment='用户-角色',
    mysql_comment='用户-角色',
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('sys_user_friend',
    sa.Column('id', mysql.VARCHAR(charset='latin1', collation='latin1_swedish_ci', length=64), nullable=False),
    sa.Column('userId', mysql.VARCHAR(charset='latin1', collation='latin1_swedish_ci', length=64), nullable=False),
    sa.Column('friendId', mysql.VARCHAR(charset='latin1', collation='latin1_swedish_ci', length=64), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('sys_menu',
    sa.Column('id', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_general_ci', length=64), nullable=False, comment='编号'),
    sa.Column('parent_id', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_general_ci', length=64), nullable=True, comment='父级编号'),
    sa.Column('name', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_general_ci', length=128), nullable=False, comment='名称'),
    sa.Column('alias', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_general_ci', length=255), nullable=True, comment='别名(meta里title字段)'),
    sa.Column('layout', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_general_ci', length=255), nullable=True, comment='布局框架'),
    sa.Column('permission', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_general_ci', length=255), nullable=True, comment='权限'),
    sa.Column('actions', mysql.TEXT(charset='utf8mb4', collation='utf8mb4_general_ci'), nullable=True, comment='操作'),
    sa.Column('icon', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_general_ci', length=30), nullable=True, comment='图标'),
    sa.Column('sort', mysql.INTEGER(), server_default=sa.text("'0'"), autoincrement=False, nullable=True, comment='排序'),
    sa.Column('create_by', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_general_ci', length=64), nullable=True, comment='创建者'),
    sa.Column('create_date', mysql.DATETIME(), nullable=True, comment='创建时间'),
    sa.Column('update_by', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_general_ci', length=64), nullable=True, comment='更新者'),
    sa.Column('update_date', mysql.DATETIME(), nullable=True, comment='更新时间'),
    sa.Column('del_flag', mysql.CHAR(charset='utf8mb4', collation='utf8mb4_general_ci', length=0), nullable=True, comment='删除标记'),
    sa.Column('remarks', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_general_ci', length=257), nullable=True, comment='描述'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('sys_role_menu',
    sa.Column('role_id', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=64), nullable=False, comment='角色编号'),
    sa.Column('menu_id', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=64), nullable=False, comment='菜单编号'),
    sa.PrimaryKeyConstraint('role_id', 'menu_id'),
    comment='角色-菜单',
    mysql_comment='角色-菜单',
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_table('sequence',
    sa.Column('name', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('current_value', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('increment', mysql.INTEGER(), server_default=sa.text("'1'"), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('name'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_table('sys_user',
    sa.Column('id', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=64), nullable=False, comment='编号'),
    sa.Column('company_id', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=64), nullable=True, comment='归属公司'),
    sa.Column('office_id', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=64), nullable=True, comment='归属部门'),
    sa.Column('login_name', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=100), nullable=True, comment='登录名'),
    sa.Column('password', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=100), nullable=True, comment='密码'),
    sa.Column('no', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=100), nullable=True, comment='工号'),
    sa.Column('name', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=100), nullable=True, comment='姓名'),
    sa.Column('email', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=200), nullable=True, comment='邮箱'),
    sa.Column('phone', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=200), nullable=True, comment='电话'),
    sa.Column('mobile', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=200), nullable=True, comment='手机'),
    sa.Column('avatar', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=1000), nullable=True, comment='用户头像'),
    sa.Column('login_ip', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=100), nullable=True, comment='最后登陆IP'),
    sa.Column('login_date', mysql.DATETIME(), nullable=True, comment='最后登陆时间'),
    sa.Column('login_flag', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=64), nullable=True, comment='是否可登录'),
    sa.Column('create_by', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=64), nullable=True, comment='创建者'),
    sa.Column('create_date', mysql.DATETIME(), nullable=True, comment='创建时间'),
    sa.Column('update_by', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=64), nullable=True, comment='更新者'),
    sa.Column('update_date', mysql.DATETIME(), nullable=True, comment='更新时间'),
    sa.Column('remarks', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=255), nullable=True, comment='备注信息'),
    sa.Column('del_flag', mysql.CHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=1), server_default=sa.text("'0'"), nullable=True, comment='删除标记'),
    sa.Column('qrcode', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=1000), nullable=True, comment='二维码'),
    sa.Column('sign', mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=450), nullable=True, comment='个性签名'),
    sa.PrimaryKeyConstraint('id'),
    comment='用户表',
    mysql_comment='用户表',
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    with op.batch_alter_table('sys_user', schema=None) as batch_op:
        batch_op.create_index('sys_user_update_date', ['update_date'], unique=False)
        batch_op.create_index('sys_user_office_id', ['office_id'], unique=False)
        batch_op.create_index('sys_user_login_name', ['login_name'], unique=False)
        batch_op.create_index('sys_user_del_flag', ['del_flag'], unique=False)
        batch_op.create_index('sys_user_company_id', ['company_id'], unique=False)

    op.drop_table('order_info')
    op.drop_table('dvadmin_system_dict')
    # ### end Alembic commands ###