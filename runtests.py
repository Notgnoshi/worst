#!/usr/bin/env python3
import nose

nose.main(argv=['',
                '--with-doctest',
                '--with-coverage',
                '--cover-html',
                '--cover-erase',
                '--cover-html-dir=htmlcov'])
