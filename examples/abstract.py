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
# # Blend NASA day and night views for AGU abstract
#
# Plot a blended image of the NASA Blue and Black marble mosaic images with a general perspective image over the New Orleans Ernest N. Morial Convention Center.
#
# Based on code written by Wei Ji Leong in https://github.com/GenericMappingTools/pygmt/issues/1395#issuecomment-891777960.
#
# Data References - Global Earth Day/Night Images:
#
# - Blue Marble: https://visibleearth.nasa.gov/images/57752/blue-marble-land-surface-shallow-water-and-shaded-topography
# - Black Marble: https://earthobservatory.nasa.gov/features/NightLights/page3.php
#

# %%
import pygmt

# %%
#Set the resolution to 2 arc minutes (30s used in abstract)
res = "02m" 

# %%
# Use the location of the Sun at 6.30am (sunrise) on 13 Dec 2021, Central Standard Time (UTC-6)
# !gmt solar -C -o0:1 -I+d2021-12-13T06:30+z-6  # -8.95331142671	-23.1626971083

# %%
# Make a global grid with a smooth 2-degree transition across day/night boundary.
# !gmt grdmath -Rd -I$res -r -8.95331142671 -23.1626971083 2 DAYNIGHT = w.nc

# %%
# Create an intensity grid based on a DEM so that we can see structures in the oceans
pygmt.grdgradient(grid=f"@earth_relief_{res}", normalize="t0.5", azimuth=45, outgrid="intens.nc")
# Mask so that the DEM-based intensity is NaN on land
# !gmt grdmath @earth_mask_$res 0 EQ 0 NAN intens.nc MUL = intens_ocean.nc

# %%
# Blend the earth_day and earth_night geotiffs using the weights, so that when w is 1
# we get the earth_day, and then adjust colors based on the intensity.
# !gmt grdmix @earth_day_$res @earth_night_$res -Ww.nc -Gview.tif -Iintens_ocean.nc

# %%
# Plot this image on an Earth with view from over New Orleans Ernest N. Morial Convention Center
fig = pygmt.Figure()
fig.grdimage(
    grid="view.tif",
    # General Perspective lon0/lat0/width+z<altitude>+a<azimuth>+t<tilt>+w<twist>+v<vwidth>/<vheight>
    projection="G-90.0631825/29.9395386/25c+z3000+a345+t10+w-30+v90/60",
    verbose="e"
)
fig.logo(position="jTR+w3c")
fig.show()

# %%
# Save the figure
fig.savefig(fname="figures/agu2021_abstract.png")
