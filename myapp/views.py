from django.shortcuts import render, HttpResponse

topics=[
    {'id':'상현달','title':'routing','body':'routing is .........'},
    {'id':'하현달','title':'view','body':'view is .........'},
    {'id':'보름달','title':'Model','body':'Model is .........'},
]
def HTMLTemplate():
    return '''
        <html lang="ko">
        <body>
        <h1>열심히 해보자구~</h1>
            <div>장고로 만든 웹페이지입니다.!</div>
            <ol>
            {ol}
            </ol>
        </body>
        </html>'''

def index(request):
    global topics
    ol = ' '
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</li>' 
    return HttpResponse(f'''
        <html lang="ko">
        <body>
        <h1>열심히 해보자구~</h1>
            <div>장고로 만든 웹페이지입니다.!</div>
            <ol>
            {ol}
            </ol>
        </body>
        </html>
                        ''')

def read(request,id):
    return HttpResponse('Read!'+id)


def create(request):
    return HttpResponse('Create')


