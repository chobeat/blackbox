FROM python:3.7-alpine
EXPOSE 5000
WORKDIR app
COPY * /app/
RUN apk add\

                       build-base \
                       # wget dependency
                       openssl \
                       # dev dependencies
                       git \
                       bash \
                       sudo \
                       # Pillow dependencies
                       jpeg-dev \
                       zlib-dev \
                       freetype-dev \
                       lcms2-dev \
                       openjpeg-dev \
                       tiff-dev \
                       tk-dev \
                       tcl-dev \
                       harfbuzz-dev \
                       fribidi-dev\
                       cmake
RUN pip install -r requirements.txt
CMD python app.py
