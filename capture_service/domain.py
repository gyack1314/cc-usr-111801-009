"""解析原始资料身份；跨来源业务关联仍待开发。"""
import json
def decode(raw, receipt):
    d=json.loads(raw.decode('utf-8'))
    if not all(key in d for key in ('kind','id','revision')):raise ValueError('资料身份缺失')
    return [{'type':d['kind'],'id':d['id'],'version':d['revision'],
             'payload':{key:value for key,value in d.items() if key not in ('kind','id','revision')}}]
def assess(rows):
    return {'publishable':False,'reasons':['来源资料已收，跨边界归属和正式闭合尚待核对'],
            'received_types':sorted({row['type'] for row in rows}),
            'received_versions':len(rows)}
