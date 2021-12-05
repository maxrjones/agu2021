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
# # Blend NASA day and night views for AGU poster background
# Data References - Global Earth Day/Night Images:
#
# - Blue Marble: https://visibleearth.nasa.gov/images/57752/blue-marble-land-surface-shallow-water-and-shaded-topography
# - Black Marble: https://earthobservatory.nasa.gov/features/NightLights/page3.php

# %%
import pygmt

# %%
#Set the resolution to 2 arc minutes
res = "05m" 
region="-270/90/-90/90"

# %%
# Use the location of the Sun at 09:00 on 13 Dec 2021, Central Standard Time (UTC-6)
# !gmt solar -C -o0:1 -I+d2021-12-13T09:00+z-6  # -46.4410128416 -23.1694592154

# %%
# Make a global grid with a smooth 2-degree transition across day/night boundary.
# !gmt grdmath -R$region -I$res -r -46.4410128416 -23.1694592154 2 DAYNIGHT = weights.nc

# %%
# Cut grids to region
pygmt.grdcut(grid=f"@earth_relief_{res}", region=region, outgrid="relief.nc")
pygmt.grdcut(grid=f"@earth_day_{res}", region=region, outgrid="day.tif")
pygmt.grdcut(grid=f"@earth_night_{res}", region=region, outgrid="night.tif")
pygmt.grdcut(grid=f"@earth_mask_{res}", region=region, outgrid="mask.nc")

# %%
# Create an intensity grid based on a DEM so that we can see structures in the oceans
pygmt.grdgradient(grid="relief.nc", normalize="t0.5", azimuth=45, outgrid="intens.nc")
# Mask so that the DEM-based intensity is NaN on land
# !gmt grdmath mask.nc 0 EQ 0 NAN intens.nc MUL = intens_ocean.nc

# %%
# Blend the earth_day and earth_night geotiffs using the weights, so that when w is 1
# we get the earth_day, and then adjust colors based on the intensity.
# !gmt grdmix day.tif night.tif -Wweights.nc -Gfigures/agu2021_background.png -Iintens_ocean.nc
