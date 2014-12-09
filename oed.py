#!/usr/bin/env python
"""

oed-xml.py - OED XML Python Query

Copyright 2014 Sujeet Akula (sujeet@freeboson.org)
Licensed under the Eiffel Forum License 2.


"""

from lxml import etree
from StringIO import StringIO
import contextlib, urllib, urllib2
from HTMLParser import HTMLParser
import re

#from urllib import urlopen, urlencode

oed = r'http://www.oed.com/srupage'
oed_url = r'http://www.oed.com/srupage?operation=searchRetrieve&query=cql.serverChoice+=+{}&maximumRecords=100&startRecord=1'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
srw = r'{http://www.loc.gov/zing/srw/}'
sru_dc = r'{info:srw/schema/1/dc-v1.1}'
dc = r'{http://purl.org/dc/elements/1.1/}'

oed_req_vals = {'operation'      : 'searchRetrieve',
                'query'          : 'cql.serverChoice = {}',
                'maximumRecords' : '100',
                'startRecord'    : '1'}
headers = { 'User-Agent' : user_agent }


#quick and dirty
rm_disp = re.compile(r'<[/]*display>')
rm_span = re.compile(r'<[/]*span[^>]*>')
sub_em = re.compile(r'<[/]*em>')
sub_strong = re.compile(r'<[/]*strong>')

hparse = HTMLParser()

def fetch(req_vals):
    oed_req = urllib2.Request(oed, urllib.urlencode(req_vals), headers)
    u = urllib2.urlopen(oed_req)
    data = u.read()
    return data

def get_id(query):
    res = search(query)

    return res[1][0][1]

def search(query):
    defs = list()

    req_vals = oed_req_vals.copy()
    req_vals['query'] = req_vals['query'].format(urllib.quote(query))
    result_xml = fetch(req_vals)

    result_tree = etree.parse(StringIO(result_xml))
    root = result_tree.getroot()

    num_records = root.find(srw + 'numberOfRecords')
    if num_records is None:
        print 'Error: Unknown number of records'
        return
    else:
        num_records = int(num_records.text)

    if num_records < 1:
        print 'Error: No records found'
        return


    records = root.find(srw + 'records').getiterator()

    for record in records:
        rdata = record.find(srw + 'recordData')
        if rdata is not None:
            data = rdata.find(sru_dc + 'dc')
            title = hparse.unescape(data.find(dc + 'title').text).encode('utf-8')
            identifier = hparse.unescape(data.find(dc + 'identifier').text).encode('utf-8')
            desc = hparse.unescape(clean_desc(data.find(dc + 'description').text)).encode('utf-8')
            defs.append([title, identifier, desc])

    return (num_records, defs)

def clean_desc(desc):
    desc = rm_disp.sub('', desc)
    desc = rm_span.sub('', desc)
    desc = sub_em.sub('/', desc)
    desc = sub_strong.sub('*', desc)
    return desc

def test():
    query = 'troglodyte'

    (num, defs) = search(query)
    print str(num) + ' record(s) found.'

    if defs is not None:
        for defn in defs:
            print(defn)

if __name__ == '__main__':
    test()


