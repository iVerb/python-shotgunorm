# Copyright (c) 2013, Nathan Dunsworth - NFXPlugins
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the NFXPlugins nor the names of its contributors
#       may be used to endorse or promote products derived from this software
#       without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL NFXPLUGINS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

__all__ = [
  'SgApiInfo'
]

# Python imports
import os

# This module imports
import ShotgunORM

class SgApiInfo(object):
  '''
  Class that represents the API information of a Shotgun connection.
  '''

  def __repr__(self):
    return '<SgApiInfo: %s>' % self.version()

  def __str__(self):
    return 'Shotgun API %s' % self.version()

  def __init__(self):
    self.__majVersion = 0
    self.__minVersion = 0
    self.__relVersion = 0
    self.__phase = 'release'
    self.__path = ''

    if ShotgunORM.SHOTGUN_API != None:
      info = ShotgunORM.SHOTGUN_API.__version__.split('.')

      self.__majVersion = int(info[0])
      self.__minVersion = int(info[1])
      self.__relVersion = int(info[2])

      if len(info) > 3:
        self.__phase = info[3]

      self.__path = os.path.dirname(ShotgunORM.SHOTGUN_API.__file__)

  def isDev(self):
    '''
    Returns True if the Shotgun API is a dev release.
    '''

    return self.__phase.lower() in ['dev', 'devel']

  def majorVersion(self):
    '''
    Returns the major version number of the Shotgun API.
    '''

    return self.__majVersion

  def minorVersion(self):
    '''
    Returns the minor version number of the Shotgun API.
    '''

    return self.__minVersion

  def phase(self):
    '''
    Returns the phase of the Shotgun API.
    '''

    return self.__phase

  def releaseVersion(self):
    '''
    Returns the release version number of the Shotgun API.
    '''

    return self.__relVersion

  def version(self):
    '''
    Returns a list of the major, minor, relase information of the Shotgun
    instance.
    '''

    if self.isDev():
      return '%d.%d.%d.%s' % (
        self.__majVersion,
        self.__minVersion,
        self.__relVersion,
        self.__phase
      )
    else:
      return '%d.%d.%d' % (
        self.__majVersion,
        self.__minVersion,
        self.__relVersion
      )
