# coding=utf-8
# Copyright 2014 Pants project contributors (see https://github.com/pantsbuild/pants/blob/master/CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see https://github.com/pantsbuild/pants/blob/master/LICENSE).

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

import os

from pants.util.contextutil import temporary_dir
from pants_test.pants_run_integration_test import PantsRunIntegrationTest


def _indent(content):
  return '\n\t'.join(content.splitlines())

class TestEnsime(PantsRunIntegrationTest):
  def _ensime_test(self, specs, project_dir=os.path.join('.pants.d', 'tmp-ensime', 'project'),
                   project_name='project'):
    """Helper method that tests ensime generation on the input spec list."""

    if not os.path.exists(project_dir):
      os.makedirs(project_dir)
    with temporary_dir(root_dir=project_dir) as path:
      pants_run = self.run_pants(['ensime', '--project-dir={dir}'.format(dir=path)] + specs)
      self.assert_success(pants_run)
      workdir = os.path.join(path, project_name)
      self.assertTrue(
        os.path.exists(workdir),
        'Failed to find project_dir at {dir}.'.format(dir=workdir))

      ensime_file = os.path.join(workdir, '.ensime')
      self.assertTrue(
        os.path.exists(ensime_file),
        'Failed to find ensime file: {ensime}\nstdout: {stdout}'.format(
          ensime=ensime_file,
          stdout=_indent(pants_run.stdout_data)))

      with open(ensime_file, 'r') as actual_ensime_file:
        return  actual_ensime_file.read()

  # Testing Ensime integration on a sample project
  def test_ensime_on_all_examples(self):
    ensime_file = self._ensime_test(['src/scala/verst/testproj/simple'])
    assert 'scala-version "2.11.' in ensime_file
