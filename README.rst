======================
django-admin-wmdeditor
======================

django-admin-wmdeditor adds a markdown wysiwym editor to your textareas in djangos admin interface.

Quick installation instruction
==============================

1. Link ``admin_wmdeditor/media/admin-wmdeditor`` in your ``MEDIA_ROOT`` as ``admin-wmdeditor`` or 
   define ``WMDEDITOR_MEDIA_PREFIX`` and make sure, the needed files are available using the given prefix.

2. Import WmdEditorModelAdmin from ``admin_wmdeditor`` and use this class instead ``admin.ModelAdmin``

3. Define ``wmdeditor_fields`` as a tuple of fields where you want to use the markdown wysiwym editor

4. Thats it. Have fun!

Example project
===============

This package provides a demo project, to show the usage of django-admin-wmdeditor.

1. Go to ``django-admin-wmdeditor/demo_project/``
2. ``$ ./manage.py syncdb`` and create a superuser
3. ``$ ./manage.py runserver`` and point your browser to ``http://127.0.0.1:8000/admin/``
4. Test the markdown wysiwym editor using the ``MyModel`` stuff.