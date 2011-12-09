#!/usr/bin/env python
# coding:utf8
from django import forms
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from django.utils import simplejson


class SmartForm(forms.Form):
    __defaults = {
            'form_id': 'id_form',
            'form_name': 'form',
            'form_class': '',
            'form_action': ''
            }
    class Media:
        js = ('jquery.js', 'jquery.form.js',)

    def __init__(self, *args, **kwargs):
        self.ajax = kwargs.pop('ajax', False)
        super(SmartForm, self).__init__(*args, **kwargs)
    
    def response_ok(self):
        return HttpResponse(simplejson.dumps({'result':'ok'}), mimetype='application/json')

    def response_bad(self):
        return HttpResponse(simplejson.dumps({'result':'bad', 'form_html': unicode(self)}), mimetype='application/json')
    
    def get_meta_val(self, key):
        val = self.__defaults.get(key)
        if hasattr(self, 'Meta'):
            val = getattr(self.Meta, key)
        return val

    def js(self):
        if not self.ajax:
            return ''
        fid = self.get_meta_val('form_id')
        output = """<script type="text/javascript">
$(document).ready(function(){
    $('form#%s').ajaxForm({
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
</script>""" % fid
        return mark_safe(output)

    def full_table(self):
        fid = self.get_meta_val('form_id')
        fname = self.get_meta_val('form_name')
        fclass = self.get_meta_val('form_class')
        faction = self.get_meta_val('form_action')
        output = u"""<form id="%s" name="%s" class="%s" action="%s" method="POST">
<table>
%s
</table>
<button type="submit" id="id_submit">确认</button>
</form>""" % \
            (fid, fname, fclass, faction, self.as_table(), )
        return mark_safe(output)
