'''OpenGL extension NV.video_capture

This module customises the behaviour of the 
OpenGL.raw.GL.NV.video_capture to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides a mechanism for streaming video data
	directly into texture objects and buffer objects.  Applications can
	then display video streams in interactive 3D scenes and/or
	manipulate the video data using the GL's image processing
	capabilities.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/video_capture.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.NV.video_capture import *
### END AUTOGENERATED SECTION