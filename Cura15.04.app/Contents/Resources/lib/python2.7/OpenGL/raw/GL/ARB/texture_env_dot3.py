'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p
from OpenGL.GL import glget
EXTENSION_NAME = 'GL_ARB_texture_env_dot3'
_p.unpack_constants( """GL_DOT3_RGB_ARB 0x86AE
GL_DOT3_RGBA_ARB 0x86AF""", globals())


def glInitTextureEnvDot3ARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
