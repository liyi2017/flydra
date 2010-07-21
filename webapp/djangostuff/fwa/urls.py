from django.conf.urls.defaults import *

urlpatterns = patterns('fwa.views',
    (r'^$', 'select_db'), # show list of databases, choose the database
    (r'^(?P<db_name>\w+)/$', 'select_dataset'), # show the datasets in database, choose dataset
    (r'^(?P<db_name>\w+)/(?P<dataset>\w+)/$', 'dataset'), # show the dataset
    (r'^(?P<db_name>\w+)/(?P<dataset>\w+)/submit_SGE_jobs/$', 'submit_SGE_jobs'), # submit CouchDB job docs to SGE
    (r'^(?P<db_name>\w+)/(?P<dataset>\w+)/DataNodes/$', 'datanodes_by_property'), # show the dataset
    (r'^(?P<db_name>\w+)/(?P<dataset>\w+)/DataNodes/(?P<property_name>[\w ]+)/$', 'datanodes_by_property'),
    (r'^(?P<db_name>\w+)/(?P<dataset>\w+)/apply_analysis_type/(?P<class_name>[\w ]+)/$', 'apply_analysis_type'),
#    (r'^(?P<db_name>\w+)/DataNode/(?P<doc_id>.*)/$', 'datanode'), # show the datanode
    (r'^(?P<db_name>\w+)/doc/(?P<doc_id>.*)/$', 'document_multiplexer'), # show the raw document
    (r'^(?P<db_name>\w+)/attachment/(?P<doc_id>.*)/(?P<fname>.*)$', 'serve_attachment'),
)