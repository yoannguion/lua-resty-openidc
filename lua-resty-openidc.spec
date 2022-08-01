%define lua_dir	%{_datarootdir}/lua
%define lua_dir_resty	%{lua_dir}/5.3/resty

Name: lua-resty-openidc
Summary: OpenID Connect Relying Party and OAuth 2.0 Resource Server implementation in Lua for NGINX / nginx-module-lua.
Version: 1.7.5
Release: 3
URL: https://github.com/yoannguion/lua-resty-openidc
License: BSD
Provides: OpenID Connect Relying Party and OAuth 2.0 Resource Server implementation in Lua for NGINX / nginx-module-lua.
Requires: lua-resty-string, lua-resty-http >= 0.16.1, lua-resty-jwt >= 0.2.3, lua-resty-session >= 3.10
BuildArch: noarch

%description
OpenID Connect Relying Party and OAuth 2.0 Resource Server implementation in Lua for NGINX / nginx-module-lua.



%install
mkdir -p $RPM_BUILD_ROOT%{lua_dir_resty}
cp -rf %{_sourcedir}/lib/resty/* $RPM_BUILD_ROOT%{lua_dir_resty}

%files
%{lua_dir_resty}/openidc.lua


%changelog
* Mon Aug 01 2022 Yoann GUION <yoann.guion@gmail.com> - 1.7.5-3
- Initial release 1.7.5
