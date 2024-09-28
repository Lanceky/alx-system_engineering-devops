# This manifest installs Flask 2.1.0 and a compatible Werkzeug version using pip3

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Install a compatible version of Werkzeug
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
