"""data_mesh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .connections import views as connections_view
from .dag_files import views as dag_files_view
from .dags import views as dags_view
from .pools import views as pools_view
from .teams import views as teams_view
from .transformations import views as transformations_view
from .variables import views as variables_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # teams
    path('api/teams/', teams_view.team_list),
    path('api/teams/<str:name>/', teams_view.team_detail),

    # team-members
    path('api/teams/<str:name>/members/', teams_view.member_list),
    path('api/teams/<str:name>/members/<str:member>/', teams_view.member_detail),

    # transformations
    path('api/transformations/', transformations_view.transformation_list),
    path('api/transformations/<str:name>/',
         transformations_view.transformation_detail),

    # dags
    path('api/dags/', dags_view.dag_list),
    path('api/dags/<str:name>/', dags_view.dag_detail),
    path('api/dags/<str:name>/trigger/', dags_view.dag_trigger),
    path('api/dags/<str:name>/backfill/', dags_view.dag_backfill),

    # dags-files
    path('api/dag-files/', dag_files_view.file_list),
    path('api/dag-files/<str:name>/', dag_files_view.file_detail),
    path('api/dag-files/<str:name>/download', dag_files_view.file_download),

    # airflow-pools
    path('api/pools/', pools_view.pool_list),
    path('api/pools/<str:name>/', pools_view.pool_detail),

    # airflow-variables
    path('api/variables/', variables_view.variable_list),
    path('api/variables/<str:name>/', variables_view.variable_detail),

    # airflow-connections
    path('api/connections/', connections_view.connection_list),
    path('api/connections/<str:name>/', connections_view.connection_detail),

]
