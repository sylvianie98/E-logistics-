#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 23:43:17 2021

@author: byc
"""

import pandas as pd
import numpy as np


from bokeh.plotting import figure, show
from bokeh.tile_providers import get_provider, Vendors
from bokeh.models import (GraphRenderer, Circle, MultiLine, StaticLayoutProvider,ColumnDataSource)


def plotNetwork(nodes, links, title='Plot of populations', target=None, on_map=False):
    """
    Plots a static map of a network = (nodes, links).
    :param nodes: pandas df with 'name', 'x', 'y' cols
                  'x' and 'y' treated as mercator coords
    :param links: pandas df with 'start' and 'end' cols
                  with entries matching nodes' names
    :param title: str of graph title
    :param target: list of node names
    :param on_map: boolean for map background
    """
    dfn = nodes
    dfl = links
    # extract data
    node_ids = dfn.name.values.tolist()
    start = dfl.start.values.tolist()
    end = dfl.end.values.tolist()
    x = dfn.x.values.tolist()
    y = dfn.y.values.tolist()
    
        
    # get plot boundaries
    min_x, max_x = min(dfn.x)+2000, max(dfn.x)-2000
    min_y, max_y = min(dfn.y)+2000, max(dfn.y)-2000
    
    plot = figure(x_range=(min_x, max_x), y_range=(min_y, max_y),
                  x_axis_type="mercator", y_axis_type="mercator",
                  title=title,
                  plot_width=600, plot_height=470,
                  toolbar_location=None, tools=[]
                 )
    
    graph = GraphRenderer()
    
    if on_map == True:
        # add map tile
        plot.add_tile(get_provider(Vendors.CARTODBPOSITRON_RETINA))
    
    # define nodes
    graph.node_renderer.data_source.add(node_ids, 'index')
    graph.node_renderer.glyph = Circle(line_color='green', line_alpha=0,
                                       fill_color='green', size=3.5,
                                       fill_alpha=0
                                      )
    
    if on_map == True:
        # add map tile
        plot.add_tile(get_provider(Vendors.CARTODBPOSITRON_RETINA))
    
    
    
    # set node locations
    graph_layout = dict(zip(node_ids, zip(x, y)))
    graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)
    
    plot.renderers.append(graph)

    # add POIS
    color = ['#99EDC3','#eddf99','#ed99ce','#5ec1ff','#1100a8']
    data = pd.read_csv('nyc_population.csv')
    po = pd.DataFrame(data)
    for i in range(0,31):
        dfp = po[po['name']==target[i]]
        source = ColumnDataSource(dfp)
        poi = Circle(x="x", y="y", size=3.5, line_color='white',
                 fill_color=color[0], line_width=0.1
                )
        plot.add_glyph(source, poi)
    for i in range(31,61):
        dfp = po[po['name']==target[i]]
        source = ColumnDataSource(dfp)
        poi = Circle(x="x", y="y", size=3.5, line_color='white',
                 fill_color=color[1], line_width=0.1
                )
        plot.add_glyph(source, poi)
    for i in range(61,91):
        dfp = po[po['name']==target[i]]
        source = ColumnDataSource(dfp)
        poi = Circle(x="x", y="y", size=3.5, line_color='white',
                 fill_color=color[2], line_width=0.1
                )
        plot.add_glyph(source, poi)
    for i in range(91,121):
        dfp = po[po['name']==target[i]]
        source = ColumnDataSource(dfp)
        poi = Circle(x="x", y="y", size=3.5, line_color='white',
                 fill_color=color[3], line_width=0.1
                )
        plot.add_glyph(source, poi)
    for i in range(121,151):
        dfp = po[po['name']==target[i]]
        source = ColumnDataSource(dfp)
        poi = Circle(x="x", y="y", size=3.5, line_color='white',
                 fill_color=color[4], line_width=0.1
                )
        plot.add_glyph(source, poi)
    for i in range(151,157):
        dfp = po[po['name']==target[i]]
        source = ColumnDataSource(dfp)
        poi = Circle(x="x", y="y", size=3.5, line_color='white',
                 fill_color=color[5], line_width=0.1
                )
        plot.add_glyph(source, poi)
    
    show(plot)
    
