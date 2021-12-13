# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# ## Quick introduction to making maps with PyGMT
#
# The tutorial introduces the plotting functionality provided by [PyGMT](https://www.pygmt.org/), which is an [open source](https://github.com/GenericMappingTools/pygmt) Python library for geospatial processing, analysis, and visualization.
#
# ### Why use PyGMT?
#
# - Process, analyze, and plot Cartesian, geographic, and/or time-series data
# - Work with NumPy, pandas, xarray, and GeoPandas objects
# - Display analysis and visualizations in Jupyter Notebooks
# - Interact with a [supportive community](https://forum.generic-mapping-tools.org/) of geospatial enthusiasts
#
# ### Import PyGMT module
#
# Run the following code cell to import the PyGMT module.

# %%
import pygmt

# %% [markdown]
# ### Task 1: Create a simple basemap
#
# The [Figure](https://www.pygmt.org/latest/api/generated/pygmt.Figure.html#pygmt.Figure) class is central to all plotting in PyGMT. The following creates an instance of the pygmt.Figure class.

# %%
fig = pygmt.Figure()

# %% [markdown]
# Here, we'll create a simple basemap using the [pygmt.Figure.basemap](https://www.pygmt.org/latest/api/generated/pygmt.Figure.basemap.html#pygmt.Figure.basemap) method. We'll use these three parameters to control the basemap appearance:
#
# - The ``region`` parameter.
#   - This parameter controls the boundaries of the plot, usually
#     by accepting a list in the form `[xmin, xmax, ymin, ymax]`.
#   - There are a few special options for the ``region`` parameter,
#     which are detailed in the [region tutorial](https://www.pygmt.org/v0.5.0/tutorials/regions.html).
# - The ``projection`` parameter.
#   - This parameter controls how your data are mapped onto a 2D
#     plot. The control over projection is what sets libraries
#     like PyGMT apart from libraries focused on
#     visualizing non-geographic datasets. There are many projections
#     options listed in the [projections table](https://www.pygmt.org/v0.5.0/projections/index.html#projection-table)
#     with examples shown in the [projections gallery](https://www.pygmt.org/v0.5.0/projections/index.html).
# - The ``frame`` parameter.
#   - This parameter controls the appearance of the map frame
#     boundary.
#   - For simple, automatic frame settings you can use ``frame=True``.
#   - There's a lot the frame parameter can do, which is detailed in the [frame tutorial](https://www.pygmt.org/v0.5.0/tutorials/frames.html).
#     
# After adding a basemap, we'll display the figure using the [pygmt.Figure.show](https://www.pygmt.org/latest/api/generated/pygmt.Figure.basemap.html#pygmt.Figure.show) method.
#

# %%
fig.basemap(region=[-180, 180, -70, 70], projection="M20c", frame=True)
fig.show()

# %% [markdown]
# ### Task 2: Plot coastlines
#
# We start off by creating a figure instance and adding a basemap, as in Task 1. This time, we'll use a shortcut for specifying a global map and the [Hammer](https://www.pygmt.org/v0.5.0/projections/misc/misc_hammer.html#sphx-glr-projections-misc-misc-hammer-py) projection. We'll then add coastlines using the [pygmt.Figure.coast](https://www.pygmt.org/latest/api/generated/pygmt.Figure.coast.html#pygmt.Figure.coast) method.
#

# %%
fig = pygmt.Figure()
fig.basemap(region="d", projection="H20c", frame=True)
fig.coast(shorelines=True)
fig.show()

# %% [markdown]
# We can use more parameters in the coast method to color lakes, rivers, land, or water.

# %%
fig = pygmt.Figure()
fig.basemap(region="d", projection="H20c", frame=True)
fig.coast(shorelines=True, land="darkgreen", water="lightsteelblue2")
fig.show()

# %% [markdown]
# ### Task 3: Plot earth relief
#
# After creating a new figure instance, we'll use the [pygmt.Figure.grdimage](https://www.pygmt.org/latest/api/generated/pygmt.Figure.grdimage.html#pygmt.Figure.grdimage) method to plot the SRTM15+V2.1 grid (Tozer et al., 2019), accessed through PyGMT's [remote dataset](https://www.generic-mapping-tools.org/remote-datasets/) functionality.

# %%
fig = pygmt.Figure()
fig.basemap(frame=True, projection="H20c", region="d")
fig.grdimage(grid="@earth_relief_20m", shading=True)
fig.show()

# %% [markdown]
# ### Find out more!
#
# * Look through the [API documentation for pygmt.Figure](https://www.pygmt.org/dev/api/generated/pygmt.Figure.html#pygmt.Figure)!
# * Try out the [PyGMT tutorials](https://www.pygmt.org/latest/tutorials/index.html)!
# * Check out the [PyGMT gallery](https://www.pygmt.org/latest/gallery/index.html)!
# * Reach out to the PyGMT Community at the [Q&A Forum](https://forum.generic-mapping-tools.org/c/questions/pygmt-q-a/11).
#                                                     
