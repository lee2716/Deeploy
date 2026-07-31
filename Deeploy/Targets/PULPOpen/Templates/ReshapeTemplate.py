# SPDX-FileCopyrightText: 2021 ETH Zurich and University of Bologna
#
# SPDX-License-Identifier: Apache-2.0

from Deeploy.Targets.Generic.Templates.ReshapeTemplate import _ReshapeTemplate

# The Generic reshape template already records the aliasing in the (directed)
# `aliases` graph, which both liveness and the tiler now consume, so no
# PULP-specific alignToContext is needed anymore.
referenceTemplate = _ReshapeTemplate("""
// Reshape (Name: ${nodeName}, Op: ${nodeOp})
${data_out} = ${data_in};
""")
