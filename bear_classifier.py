from fastai.basic_train import load_learner
from fastai.vision import open_image
from starlette.applications import Starlette
from io import BytesIO
from starlette.responses import JSONResponse
from starlette.routing import Route

# load the learner
learn = load_learner(path='./', file='export.pkl')
classes = learn.data.classes

async def homepage(request):
    return JSONResponse({'hello': 'world'})


def predict_single(img_file):
    'function to take image and return prediction'
    _,category,losses = learn.predict(open_image(BytesIO(img_file)))
    probs_list = losses.numpy()
    print('Predicted: ' + classes[category.item()])
    return {
        'category': classes[category.item()],
        'probs': {c: round(float(probs_list[i]), 5) for (i, c) in enumerate(classes)},
        'text': 'That looks like a ' + classes[category.item()]
        # ,'result': sorted(
        #     zip(learn.data.classes, map(float, losses)),
        #     key=lambda p: p[1],
        #     reverse=True
        # )

    }

# route for prediction
# @app.route('/predict', methods=['POST'])
async def predict(request):
    form = await request.form()
    filename = form["image"].filename
    contents = await form['image'].read()
    return JSONResponse(predict_single(contents))

# async def classify_url(request):
#     bytes = await get_bytes(request.query_params["url"])
#     img = open_image(BytesIO(bytes))
#     _,_,losses = learner.predict(img)
#     return JSONResponse({
#         "predictions": sorted(
#             zip(cat_learner.data.classes, map(float, losses)),
#             key=lambda p: p[1],
#             reverse=True
#         )
#     })


routes = [
    Route("/", endpoint=homepage),
    Route("/predict", predict, methods=['POST']),
    # Route("/classify-url", classify_url)
]

app = Starlette(debug=True, routes=routes)
