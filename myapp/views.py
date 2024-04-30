from django.shortcuts import render, HttpResponse,  redirect
from django.views.decorators.csrf import csrf_exempt

nextId =4
topics=[
    {'id':1,'title':'routing','body':'상현달 is .........'},
    {'id':2,'title':'view','body':'하현달 is .........'},
    {'id':3,'title':'Model','body':'보름달 is .........'},
]
def HTMLTemplate(articleTag, id=None):
    global topics
    contextUI =''
    if id != None:
        contextUI =f'''
        <li>
                            <form action="/delete/" method="post">
                            <input type="hidden" name="id" value={id}>
                                        <input type="submit" value="delete">
                            </form>
                    </li>
        '''
    ol = ' '
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>' 
    return f'''
        <html lang="ko">
        <body>
        <h1>열심히 해보자구~</h1>
            <div>장고로 만든 웹페이지입니다.!</div>
            <ol>
                {ol}
            </ol>
            {articleTag}
            <ul>
                    <li><a href="/create/">create</a></li>
                    {contextUI}
            </ul>
        </body>
        </html>'''

def index(request):
    article ='''
    <h2>Welcome</h2>
    Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))

def read(request,id):
    global topics
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article ,id))

@csrf_exempt
def create(request):
    global nextId
    print('request.method', request.method)
    if request.method =='GET':
        article='''
                <form action="/create/" method="post">
                    <div><input type="text" name="title" placeholder="title"></div>
                    <div><textarea name="body" placeholder="body"></textarea></div> 
                    <div><input type="submit"></div>
                </form>
                '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method =='POST':
        title = request.POST['title']
        body = request.POST['body']
        newTopic ={"id":nextId,"title":title,"body":body}
        topics.append(newTopic)
        url = '/read/'+str(nextId)
        nextId =nextId +1
        return redirect(url)

def delete(request):
    if request.method=='POST':
        id = request.POST['id']
        newTopics =[]
        for topic in topics:
            if topic['id'] != int(id):
                newTopics.append(topic)
        topic = newTopics
        return redirect('/')

