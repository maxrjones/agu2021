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
# # Stacking automatically generated cross-profiles
#
# This example is based on the Generic Mapping Tool's example 33 (https://docs.generic-mapping-tools.org/latest/gallery/ex33.html).
#
# Data from Tozer et al., 2019 (http://dx.doi.org/10.1029/2019EA000658) provided via `earth_relief_01m`.
#
# import numpy as np
# import pandas as pd

# %%
import pygmt

# %%
# Extract a subset of earth_relief_01m for the East Pacific Rise
grid = pygmt.grdcut("@earth_relief_01m", region=[-118, -107, -49, -42])

# %%
# Plot the grid subset
fig = pygmt.Figure()
pygmt.makecpt(cmap="bukavu", series=[-5000, -2000])
fig.grdimage(grid=grid, projection="M15c", shading="a15+ne0.75", frame=True)
fig.text(
    text=r"Data from Tozer et al., 2019",
    position="cBR",
    offset="0/-1.2c",
    font="12p,Helvetica",
    no_clip=True,
)
fig.show()

# %%
# Select two points along the ridge
points = np.array([[-111.6, -43.0], [-113.3, -47.5]])

# %%
# Plot ridge segment and end points
fig.plot(data=points, pen="2p,darkorange")
fig.plot(data=points, style="c0.25c", color="darkorange")
fig.show()

# %%
# Generate cross-profiles 400 km long, spaced 10 km, samped every 2km and stack these using the median
pygmt.grdtrack(
    points=points,
    grid=grid,
    crossprofile="400k/2k/10k+v",
    stack='m+s"stack.txt"',
    outfile="profiles.txt",
)

# %%
# Plot the cross-profiles
fig.plot(data="profiles.txt", pen="0.75p")
fig.show()

# %%
# Create an envelope
upper = pd.read_csv(
    "stack.txt", sep="\t", header=None, usecols=[0, 5], names=["Distance", "Value"]
)
lower = pd.read_csv(
    "stack.txt", sep="\t", header=None, usecols=[0, 6], names=["Distance", "Value"]
)
envelope = pd.concat([upper, lower[::-1]], ignore_index=True)

# %%
fig.shift_origin(yshift="h+2c")
fig.plot(
    data=envelope,
    region=[-200, 200, -3500, -2000],
    projection="X15c/7.5c",
    color="lightgrey",
    frame=['xafg1000+l"Distance from ridge (km)"', 'yaf+l"Depth (m)"', "WSNE"],
)
fig.plot(
    data="stack.txt",
    region=[-200, 200, -3500, -2000],
    projection="X15c/7.5c",
    pen="3p",
    frame=['xafg1000+l"Distance from ridge (km)"', 'yaf+l"Depth (m)"', "WSNE"],
)
fig.show()

# %%
# Save the example figure
fig.savefig("figures/profiles_ex33.png")
