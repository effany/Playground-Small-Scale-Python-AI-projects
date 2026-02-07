import tornado.ioloop
import tornado.web
import os 
import handler_module

def make_app():
    base_dir = os.path.dirname(__file__)
    template_dir = os.path.join(base_dir, 'templates')
    static_dir = os.path.join(base_dir, 'static')

    return tornado.web.Application(
        [
            (r"/", handler_module.HomeHandler),
            (r"/submit-text", handler_module.SubmitTextHandler),
            (r"/record", handler_module.RecordHandler)
            
        ],
        template_path = template_dir,
        static_path = static_dir,
        debug = True
    )

if __name__ == '__main__':
    app = make_app()
    port = 8888
    app.listen(port)
    print(f"Server is running at http://localhost:{port}")
    tornado.ioloop.IOLoop.current().start()