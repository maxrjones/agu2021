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
# # Evaluation of spherical harmonics coefficients
# This example is based on the Generic Mapping Tool's example 39 (https://docs.generic-mapping-tools.org/latest/gallery/ex39.html).
#
# The data is truncated from http://www.ipgp.fr/~wieczor/SH/VenusTopo180.txt.zip; Wieczorek, M. A., Gravity and topography of the terrestrial planets, Treatise on Geophysics, 10, 165-205, doi:10.1016/B978-044452748-6/00156-5, 2007

# %%
import pygmt

# %%
# Evaluate the global grid based on a spherical harmonic model for the topography of Venus based on Wieczorek (2007)
# Use three sets of upper order/degrees (30, 90, and 180)
grid_30d = pygmt.sph2grd(
    data="@VenusTopo180.txt", spacing=1, region="g", N="g", F="1/1/25/30"
)
grid_90d = pygmt.sph2grd(
    data="@VenusTopo180.txt", spacing=1, region="g", N="g", F="1/1/25/90"
)
grid_180d = pygmt.sph2grd(
    data="@VenusTopo180.txt", spacing=1, region="g", N="g", F="1/1/25/180"
)

# %%
# Create a figure
fig = pygmt.Figure()
# Configure the background color to match the AGU poster
pygmt.config(PS_PAGE_COLOR="#efeeee", GMT_VERBOSE="e")
# Create a colormap based on the 90 order/degrees model
pygmt.grd2cpt(cmap="vik+h0", grid=grid_90d, nlevels=True)
# Plot the first example on the bottom right
fig.shift_origin(xshift="7.5c")
fig.grdimage(
    grid=grid_30d,
    shading="a45+nt0.75",
    projection="G90/30/12c",
    frame="g",
    region="g",
    cmap=True,
)
# Add citation
fig.text(
    text=r"Data based on Wieczorek (2007)",
    position="cBL",
    offset="-3.5c/0c",
    font="12p,Helvetica",
    no_clip=True,
)
# Create a colorbar
fig.colorbar(frame=["xaf", 'y+l"m"'], position="x3c/-0.5c+jTC+w13c/0.25c+h")
# Plot the second example shifted upwards with a title
fig.shift_origin(xshift="-3c", yshift="5c")
pygmt.config(MAP_TITLE_OFFSET="5.5c")
fig.grdimage(
    grid=grid_90d,
    shading="a45+nt0.75",
    frame=["g", '+t"Venus Spherical Harmonic Model"'],
    cmap=True,
)
# Plot the third example shifted updwards
fig.shift_origin(xshift="-3c", yshift="5c")
fig.grdimage(grid=grid_180d, shading="a45+nt0.75", frame="g", cmap=True)
fig.show()

# %%
# Save the example figure
fig.savefig("figures/harmonics_ex39.png")
