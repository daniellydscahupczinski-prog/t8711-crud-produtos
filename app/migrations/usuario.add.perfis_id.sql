alter table usuario add column perfis_id integer not null,
alter table usuario add constraint fk_perfis_usuario foreign key (perfis_id) references perfis(id);