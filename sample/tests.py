#!/usr/bin/env python
# coding:utf8
"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)

__test__ = {"doctest": u"""
>>> from forms import SampleForm
>>> form = SampleForm(ajax=True)
>>> print form.full_table()
<form id="id_form" name="form" class="" action="" method="POST">
<table>
<tr><th><label for="id_username">Username:</label></th><td><input type="text" name="username" id="id_username" /></td></tr>
<tr><th><label for="id_password">Password:</label></th><td><input type="password" name="password" id="id_password" /></td></tr>
<tr><th><label for="id_password_again">Password again:</label></th><td><input type="password" name="password_again" id="id_password_again" /></td></tr>
</table>
<button type="submit" id="id_submit">确认</button>
</form>
>>> print form.js()
<script type="text/javascript">
$(document).ready(function(){
    $('form#id_form').ajaxForm({
        dataType:'json',
        success: function(data){
            if (data.result == 'ok') {
                alert('ok');
            } else {
                $('form table').html(data.form_html);
            }
        },
    });
});
</script>
>>>
""",
}

