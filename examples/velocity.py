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
# # Plot velocity vectors using PyGMT
# Based on example by Leonardo Uieda in https://github.com/leouieda/aogs2018-gmtpython.
#
# Data downloaded from https://data.unavco.org/archive/gnss/products/velocity/; This material is based on services provided by the GAGE Facility, operated by UNAVCO, Inc., with support from the National Science Foundation and the National Aeronautics and Space Administration under NSF Cooperative Agreement EAR-1724794."

# %% [markdown]
# ## Process the data to make it easier to plot

# %%
import numpy as np
import pandas as pd
import pygmt

# %%
data = pd.read_csv("data/cwu.final_nam14.vel", skiprows=35, delim_whitespace=True)
data.head()

# %%
# Remove the large East velocities
data = data[data["dE/dt"].abs() < 0.05]

# %%
# Calculate azimuth and intensity
azimuth = np.rad2deg(np.arctan2(data["dE/dt"], data["dN/dt"]))
velocity = np.hypot(data["dE/dt"], data["dN/dt"])

# %%
# Store result in a DataFrame
data = pd.DataFrame(
    dict(
        lon=data.Ref_Elong,
        lat=data.Ref_Nlat,
        velocity_east=data["dE/dt"],
        velocity_north=data["dN/dt"],
        azimuth=azimuth,
        velocity=velocity,
    ),
    columns="lon lat velocity_east velocity_north azimuth velocity".split(),
)
data.head()

# %% [markdown]
# ## Plot the velocity vectors on a general perspective map

# %%
# Format the argument for the map projection
proj = "G{lon}/{lat}/20i+z{alt}+a{azim}+t{tilt}+w{twist}+v{width}/{height}".format(
    lon=-138, lat=40, alt=1000, azim=20, tilt=40, twist=-10, width=142, height=100
)

# %%
# Start a new figure
fig = pygmt.Figure()
# Configure the background color
pygmt.config(PS_PAGE_COLOR="#efeeee", GMT_VERBOSE="e")
# Plot a hill shaded image of the builtin topography data
fig.grdimage(
    "@earth_relief",
    region=[-140, -110, 20, 60],
    projection=proj,
    cmap="ocean",
    shading="+a120+nt1.5",
)
# Fill in the continents with a gray color
fig.coast(land="#444444", resolution="i", area_thresh="0/0/1")
# Plot the velocity as vectors given an azimuth and length
fig.plot(
    x=data.lon,
    y=data.lat,
    direction=(data.azimuth, data.velocity * 50),
    style="V0.03i+e",
    color="#eeeeee",
    pen="thinnest,#eeeeee,solid",
)
# Add citations
fig.text(
    text=r"Based on Uieda and Wessel (2018)",
    position="cBL+jTR",
    font="14p,Helvetica,#111111",
    offset="20i/7.25i",
    no_clip=True,
)
fig.text(
    text=r"Data from the GAGE Facility, operated by UNAVCO, Inc.",
    position="cBL+jTR",
    font="14p,Helvetica,#111111",
    offset="20i/7i",
    no_clip=True,
)
# Display the figure
fig.show(width="100%")

# %%
# Save the example figure
fig.savefig("figures/vectors.png")
