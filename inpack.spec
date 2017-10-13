[project]
name = memcached
version = 1.5.2
vendor = memcached.org
homepage = http://memcached.org
groups = dev/db
description = high-performance, distributed memory object caching system

%build

PREFIX="{{.project__prefix}}"

cd {{.inpack__pack_dir}}/deps

if [ ! -f "memcached-{{.project__version}}.tar.gz" ]; then
    wget http://memcached.org/download/memcached-{{.project__version}}.tar.gz
fi
if [ -d "memcached-{{.project__version}}" ]; then
    rm -rf memcached-{{.project__version}}
fi
tar -zxf memcached-{{.project__version}}.tar.gz

cd memcached-{{.project__version}}

./configure --prefix=/home/action/apps/memcached
make -j2

rm -rf   {{.buildroot}}/*
mkdir -p {{.buildroot}}/{bin,run}

install memcached             {{.buildroot}}/bin/memcached
strip -s {{.buildroot}}/bin/memcached


%files

